# in what conditions should we check OnLine? 
# checks whether the rover is on the tangent line or not

def OnLine(pos_x, pos_y, xvect, yvect):
    # return bool value (T/F)
    if pos_y == ((xvect)*(pos_x) + yvect):
        return True
    else:
        return False
"""
if OnLine(x,y,xv,yv) == True:
    print("Works")

else:
    print("Doesn't")
"""
