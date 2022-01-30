
########---------- SET UP -----------######
from qset_lib import Rover

rover = Rover()  # Gets the rover

import math

shift_l = 0

num_r = 0

num_l = 0

x_final = int(input("Enter the x value of the destination: "))  # Gives the x and y coordinates of the destination
y_final = int(input("Enter the y value of the destination: "))

destination = [x_final, y_final]  # Puts them into a list

print("Destination: ", destination)

x_rover = rover.x  # Gets the initial x and y coordinates of the rover
y_rover = rover.y

rover_pos = [x_rover, y_rover]

print("Rover Position: ", rover_pos)

speed = 1  # when we figure out what the max angular speed of the rover is that will be our value.

arbitrary = [x_rover + 1, y_rover]  # acts as x-axis from rover origin

turn_angle = 0.01  # Gives initial value to turn angle

left = False
right = True

phase = 1


def Dot_product(rover_pos, destination, arbitrary):  # Calculates the dot product between 2 vectors

    vector_x = destination[0] - rover_pos[0]
    vector_y = destination[1] - rover_pos[1]
    vector_a = [vector_x, vector_y]
    length_a = math.sqrt((vector_a[0]) ** 2 + (vector_a[1]) ** 2)

    vector_x1 = arbitrary[0] - rover_pos[0]
    vector_y1 = arbitrary[1] - rover_pos[1]
    vector_b = [vector_x1, vector_y1]
    length_b = math.sqrt((vector_b[0]) ** 2 + (vector_b[1]) ** 2)

    dot_product = (vector_a[0] * vector_b[0]) + (vector_a[1] * vector_b[1])
    angle = math.acos(dot_product / (length_a * length_b))

    if destination[1] >= rover_pos[1]:
        return angle
    else:
        return -angle


def Rotate(angle, sign):  # Rotates the Rover
    beta = abs(angle)
    heading = rover.heading
    if sign == "pos":
        turn = speed
    elif sign == "neg":
        turn = -speed
    while beta > 0.017:
        rover.send_command(0, turn)
        adjustment = abs(abs(heading) - abs(rover.heading))
        beta = beta - (adjustment * (math.pi / 180))
        heading = rover.heading

run = True
while run == True:

    while phase == 1:  ########---------- PHASE 1: INITIAL START UP -----------######
        print("Now in Phase 1")
        for i in range(0,10000):
            rover.send_command(0, 0)
        if run == False:
            break
            
        while abs(turn_angle) > 0 and abs(turn_angle) < 0.017:  # It turns clockwise and counter clockwise untill it reaches the desired angle
            x_rover = rover.x  # Gets the initial x and y coordinates of the rover
            y_rover = rover.y
            rover_pos = [x_rover, y_rover]
            arbitrary = [x_rover + 1, y_rover]  # acts as x-axis from rover origin

            alpha = Dot_product(rover_pos, destination, arbitrary)
            turn_angle = (rover.heading * (math.pi / 180)) - alpha
            if turn_angle > 0:
                Rotate(abs(turn_angle), "neg")
            elif turn_angle < 0:
                Rotate(abs(turn_angle), "pos")
                
        turn_angle = 0.01
        phase = 2

    while phase == 2:  ########---------- PHASE 2: MOVING -----------######
        if abs(abs(rover.x) - abs(x_final)) < 2 and abs(abs(rover.y) - abs(y_final)) < 2:
            run = False
            print("End the loop")
        if run == False:
            break
        lasers = list(rover.laser_distances)
        if lasers[7] < 5 or lasers[6] < 4 or lasers[8] < 4 or lasers[5] < 3 or lasers[9] < 3 or lasers[4] < 2 or lasers[10] < 2:  # if the middle laser is 20m from obstacle we move onto phase 3
            print("Object Detected 0")
#             for i in range(0, 10000):
#                 rover.send_command(0, 0)
            phase = 3

        for i in range(0, 10000):
            rover.send_command(1, 0)  # Move the rover forward


    while phase == 3:  ########---------- PHASE 3: PICK DIRECTION -----------######
        print("Now in Phase 3")
        if run == False:
            break
        temp_dist = list(rover.laser_distances)  # Saves laser distances to a variable list
        dist = temp_dist[7]  # Gets the distance from the middle laser

        for i in range(0, 15):  # goes through the list looking for the the first non inf value
            if temp_dist[i] < 15:
                num_r = i
                break

        for i in range(14, 0, -1):  # does the same thing from the left side
            if temp_dist[i] < 15:
                num_l = i
                shift_l = 14 - num_l
                break

        if shift_l > num_r:  # if there is more "free" lasers on the left side move left
            print("move left")
            rover.send_command(0, 0)
            turn = num_l - 6
            gamma = turn * 6 * (math.pi / 180)
            Rotate((gamma + (math.pi) / 4), "pos")
            direction = False
            phase = 4

        else:
            print("move right")
            rover.send_command(0, 0)
            turn = -num_r + 8
            gamma = turn * 6 * (math.pi / 180)
            Rotate((gamma + (math.pi) / 4), "neg")
            direction = True
            phase = 4
        while phase == 4:  ########---------- PHASE 4: OBSTACLE AVOIDANCE -----------######
            print("Now in Phase 4")
            if phase == 1:
                break
            if run == False:
                break

            for i in range(0, 11000):
                rover.send_command(100, 0)

            index = list(rover.laser_distances)  # sensor values will be here
            if direction == True:
                while index[14] < 15 and index[11] < 15:
                    rover.send_command(300, 0)
                    index = list(rover.laser_distances)
                    if index[7] < 5 or index[6] < 4 or index[8] < 4 or index[5] < 3 or index[9] < 3 or index[4] < 2 or index[10] < 2:  # if the middle laser is 20m from obstacle we move onto phase 3
                        print("Object Detected 1")
                        rover.send_command(0,0)
                        phase = 1
                        break
                for i in range(0, 10000):
                    index = list(rover.laser_distances)
                    if index[7] < 5 or index[6] < 4 or index[8] < 4 or index[5] < 3 or index[9] < 3 or index[4] < 2 or index[10] < 2:  # if the middle laser is 20m from obstacle we move onto phase 3
                        print("Object Detected 2")
                        rover.send_command(0, 0)
                        phase = 1
                        break
                for i in range(0,11000):
                    rover.send_command(100,0)
                phase = 1
            if direction == False:
                while index[0] < 15 and index[5] < 15:
                    rover.send_command(300, 0)
                    index = list(rover.laser_distances)
                    if index[7] < 5 or index[6] < 4 or index[8] < 4 or index[5] < 3 or index[9] < 3 or index[4] < 2 or index[10] < 2:  # if the middle laser is 20m from obstacle we move onto phase 3
                        print("Object Detected 3")
                        rover.send_command(0, 0)
                        phase = 1
                        break
                for i in range(0, 10000):
                    index = list(rover.laser_distances)
                    if index[7] < 5 or index[6] < 4 or index[8] < 4 or index[5] < 3 or index[9] < 3 or index[4] < 2 or index[10] < 2:  # if the middle laser is 20m from obstacle we move onto phase 3
                        print("Object Detected 4")
                        rover.send_command(0, 0)
                        phase = 1
                        break
                    rover.send_command(100, 0)
                for i in range(0,11000):
                    rover.send_command(100,0)
                phase = 1

print(rover.x, rover.y)
print("Arrived")
for i in range(0, 10000):
    rover.send_command(0, 0)
for i in range(0,10000000):
    rover.send_command(0,1000)
