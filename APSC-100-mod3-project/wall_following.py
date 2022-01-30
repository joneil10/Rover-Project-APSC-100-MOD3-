import math
import random


spacing = 10 # distance robot should be away from wall
index = [] # sensor values will be here

direction = True #boolean to see if wall will be on let or right side. Wall being on the left will be defult
left = True #check if wall is on the left of rover




# create empty list, this is placeholder for the 15 sensor readings
for i in range(15):

    index.append(random.randint(0,20)) #inserting completely random values into list



def check_distance(distance, sensor, direction):

    if direction == left:
        reading = sensor[14] * math.cos(math.pi/4) #indexing different sensors depending on where wall is
        tooClose = distance >= reading
    else:
        reading = sensor[0] * math.cos(math.pi / 4)
        tooClose = distance >= reading

    return(tooClose)


def navigate(tooClose, direction):
    roverHeading = 0  # import from other section of code, direction rover is heading
    adjustment = 5  # how fast angle will change
    
    if direction == left: #wall is to the left
         if tooClose == True:
             #increase angle to make rover vear right, and decrease angle to make it vear left?
             roverHeading += adjustment
         else:
             roverHeading -= adjustment
    else: #wall is to the right
        if tooClose == True:
            roverHeading -= adjustment
        else:
            roverHeading += adjustment


tooClose = check_distance(spacing, index, direction)
navigate(tooClose, direction)

# missing:
# function to determine whether to turn left or right
# function/ section to check for when to exit