print("k! = 1*2*3*4*5*6*...*k")
e = 1
f = 1
k = int(input("k: "))
for k in range(1, k + 1):
    e *= f
    f+=1
print(e)