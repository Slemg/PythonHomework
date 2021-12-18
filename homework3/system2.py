import math


x = int(input("Введите x "))
if x >= 0 and x < 2:
    y = math.sqrt(math.fabs(x-5,4))
    y **= 2
 
elif x >= 2 and x < 8:
   y = math.atan(x)**2
else:
    y = math.log10(x)
    
print(y)
