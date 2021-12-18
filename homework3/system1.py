import math
p = -math.cos(1)**2

x = int(input("Введите x "))
if x > (-math.pi) and x < math.pi/4:
    y = p*x + math.cos(1)**2 * math.pi
 
elif x >= math.pi/4 and x <=1:
    module = math.fabs(x+1)
    y = math.sqrt({module})
else:
    y = 1/x-1
    
print(y)

