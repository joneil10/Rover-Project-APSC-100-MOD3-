import random  # imports stuff we need
import math
import time

phase = 1

x_final = int(input("Input x-coordinate of destination: "))   # will be constant the entire time
y_final = int(input("Input y-coordinate of destination: "))
destination = [x_final, y_final]

def Magnitude(vector):                     # Determines the magnitude of a given vector

    length = math.sqrt((vector[0])**2 + (vector[1])**2)
    return length


def Dot_product(rover_pos, destination, arbitrary):            # all 3 functions in 1, my comp sci teacher would lose it if she saw this abomination

    vector_x = rover_pos[0] - destination[0]
    vector_y = rover_pos[1] - destination[1]
    vector_a = [vector_x, vector_y]
    length_a = math.sqrt((vector_a[0])**2 + (vector_a[1])**2)

    vector_x1 = rover_pos[0] - arbitrary[0]
    vector_y1 = rover_pos[1] - arbitrary[1]
    vector_b = [vector_x1, vector_y1]
    length_b = math.sqrt((vector_b[0]) ** 2 + (vector_b[1]) ** 2)

    dot_product = (vector_a[0] * vector_b[0]) + (vector_a[1] * vector_b[1])
    angle = math.acos(dot_product / (length_a * length_b))
    return angle


#Start of main code

while rover_pos != destination:

    #Calculate heading phase

    while phase == 1:

        x_rover = rover.x
        y_rover = rover.y

        if x_final > x_rover:
            x_arbitrary = (-math.sin(rover.heading*(math.pi/180)) + x_rover)  # use the angle to determine another point on the line.
            y_arbitrary = (math.cos(rover.heading(math.pi/180)) + y_rover)
        elif x_final < x_rover:
            x_arbitrary = (Magnitude(rover_pos) - 1)*math.sin(rover.heading)  # use the angle to determine another point on the line.
            y_arbitrary = (Magnitude(rover_pos) - 1)*math.cos(rover.heading)

        rover_pos = [x_rover, y_rover]           # points that are coordinates from given values
        arbitrary = [x_arbitrary, y_arbitrary]

        time_end = time.time() + 1          #save a variable of current time and adds 1 second
        
        alpha = Dot_product(rover_pos,destination,arbitrary)
        
        while time.time() < time_end:
            if x_final> x_rover:
                rover.send_command(0,alpha)  
            elif x_final < x_rover:
                rover.send_command(0, alpha+math.pi)  #if we make rot speed alpha rads/s for 1s it should rotate alpha rad to line up w/ destination, right?
        rover.send_command(0,0)
        beta = alpha*(180/math.pi)
        if 0 <= beta <= 2:              # When the angle b/w the 2 vectors is around 0 we move on to phase 2
            phase = 2

    # Moving phase
    while phase == 2:
        if rover.laser_distance[7] < 10:     # if the middle laser is 10m from obstacle we move on to phase 2 we can index lasers yeah? Well we're gonna try.
            rover.send_command(0,0)
            phase = 3
        rover.send_command(299792458,0)           # moves the rover at light speed.

# Obstacle navgiation phase, idk what im doing.
    while phase == 3:
        temp_dist = rover.laser_distance    # saving current laser distances to temp variable
        lenght = len(temp_dist)
        for i in range(0, lenght):  # goes through the list looking for the the first non inf value
            if type(temp_dist[i]) == int:
                left = temp_dist[i]
                num_l = i           # number of lines from the end
                break
        for i in range(lenght - 1, 1, -1):  # does the same thing from the right side
            if type(temp_dist[i]) == int:
                right = temp_dist[i]
                num_r = i
                break
        if left > right:
            # move right
            shift = num_r - 7       # num of lines from middle
            gamma = (shift+1) * 6 * (math.pi / 180)     # angle to rotate that it will no longer be directly looking at obstacle
            time_end = time.time() + 1
            while time.time() < time_end:           # rot by that angle
                rover.send_command(0,gamma)
            rover.send_command(0, 0)
            while rover.laser_distance[0] < 10:         # run until you escape the obstacle
                rover.send_command(299792458,0)
            rover.send_command(0,0)
            phase = 1

        else:
            # move left, same deal as above just opp
            print("move left")
            print(num_l)
            shift = 7 - num_l
            print(shift)
            gamma = (shift+1) * 6 * (math.pi / 180)
            time_end = time.time() + 1
            while time.time() < time_end:
                rover.send_command(0, -gamma)
            rover.send_command(0, 0)
            while rover.laser_distance[14] < 10:
                rover.send_command(299792458,0)
            rover.send_command(0,0)
            phase = 1

if rover_pos == destination:       # I doubt we'll ever get this far but if we do then WE DID IT WOOOO!!!
    rover.send_command(0,299792458)
    print("We did it!!!")
