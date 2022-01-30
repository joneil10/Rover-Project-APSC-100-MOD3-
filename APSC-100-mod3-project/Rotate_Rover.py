import time
import math
x_final = -9   # will be constant the entire time
y_final = 36
destination = [x_final, y_final]

x_rover = 7
y_rover = -5

rover_pos = [x_rover,y_rover]
speed = x # when we figure out what the max angular speed of the rover is that will be our x value.

arbitrary = [x_rover+1,y_rover]         # acts as x-axis from rover origin

def Rotate(angle,sign):                     # Rotates the Rover

    rot_time = angle/speed
    if sign == pos
        turn = speed
    elif sign == neg
        turn = -speed
    time_end = time.time() + rot_time
    while time.time() < time_end:
        rover.send_command(0, turn)
    rover.send_command(0, 0)

    
while abs(turn_angle) > 0 and abs(turn_angle) < 0.17:   #It turns clockwise and counter clockwise untill it reaches the desired angle
    
    alpha = Dot_product(rover_pos,destination,arbitrary)
    turn_angle = (rover_heading*(math.pi/180))-alpha
    if turn_angle > 0:
        Rotate(abs(turn_angle),neg)
    elif turn_angle < 0:
        Rotate(abs(turn_angle),pos)
