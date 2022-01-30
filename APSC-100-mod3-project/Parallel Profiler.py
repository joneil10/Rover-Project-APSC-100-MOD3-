def lines (l1, l2): # l1- obstacle line, l2- rover line
  if(l1[1]!=0 and l2[1]!=0): #makes sure that lines are not = 0
    if(l1[0]/l1[1]==l2[0]/l2[1]): #Check slope - if equal they are parallel (rise/run)
      return True
    else:
      return False
  else:
    if(l1[0]==l2[0] and l1[1]==l2[1]): #are the lines the same line?
      return True
    else:
      return False
l1=[]
l2=[]
print("Insert the values of x1 y1 :") #test code (tested in Desmos)
for i in range(3):
        x=int(input())
        l1.append(x)
print("Insert the values of x2 y2 :")
for i in range(3):
        x=int(input())
        l2.append(x)
if(lines (l1,l2)==True):
        print("Yes")
else:
        print("No")
