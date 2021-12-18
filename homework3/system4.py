import math


x = int(input("Введите x "))
y = int(input("Введите y "))
if math.fabs(x*y) < 1 and x < 0:
    z = z+y / math.pow(math.e, x*y)
    
 
elif x and y > 2 and x and y <= 0:
   z = -(math.e**2)*x
else:
    z = math.log10(x) * math.sqrt(y)
    
print(y)
