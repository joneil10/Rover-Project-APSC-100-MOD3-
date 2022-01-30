## create start to endpoint vector
import numpy as np
import math

def endpointvector(xr,yr,xg,yg,x0,y0):
    rover_position = [xr,yr]
    endpoint = [xg,yg]
    B = [x0,y0] ## Arbitrary vector the rover is facing

    A = [endpoint[0] - rover_position[0], endpoint[1] - rover_position[1]] ## Our start to end vector

    A_length = np.linalg.norm(A) ## length of start to end vector
    B_length = np.linalg.norm(B) ## length of vector rover is currently headed in

    alpha = np.arccos((np.dot(A,B))/(A_length*B_length))*(180/math.pi) ## angle between A and B (i.e. the angle the rover must turn)

    print("The tangent vector from start to endpoint: ", A)
    print("Starting displacement: ", format(A_length, '.2f'), "m")
    print("Now turning angle of:", format(alpha,'.2f'), "degrees.")
    return alpha

# Example input:
# vector1 = endpointvector(1,2,3,4,5,6)
# print(vector1)
#
# Example Output:
# The tangeng vector from star to endpoint: [2,2]
# Starting displacement: 2.83 m
# Now turning angle of: 5.19 degrees
