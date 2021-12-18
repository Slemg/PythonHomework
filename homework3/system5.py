import math


x = int(input("Введите x "))
if x >= 1:
    y = math.e ** -(math.fabs(x))
    
 
elif math.fabs(x) < 1:
   y = math.log10(math.sqrt(1-x**2))
else:
    y = math.atan(x)
    
print(y)
