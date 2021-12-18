import math


x = int(input("Введите x "))
if math.fabs(x) < 2:
    y = x-math.e**x
    
 
elif x <= -2:
   y = math.log10(x**2)
else:
    y = math.sin(x)**2
    
print(y)
