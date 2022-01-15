import math


x = int(input("Введите x "))
if x > (-math.pi) and x < math.pi/4:
    y = -math.cos(x -math.pi)**2
 
elif x >= math.pi/4 and x <=1:
    module = math.fabs(x+1)
    y = math.sqrt({module})
elif x>1:
    y = 1/x-1
else:
   y =  print("Error")
    
print(y)

