import math
y = -math.cos(1)**2

x = int(input("Введите x "))
if x > (-math.pi) and x < math.pi/4:
    p = y*x + math.cos(1)**2 * math.pi
 
elif x >= math.pi/4 and x <=1:
    module = math.fabs(x+1)
    p = math.sqrt({module})
else:
    p = 1/x-1
    
print(p)