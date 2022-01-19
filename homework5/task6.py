x = 1
s = 0
a = 0.5
print("S = 1/2 + 1/4 + 1/8 + 1/16 + 1/32 ....... + n")
n = int(input("Введите n: "))
for x in range(1, n+1):  
    s+=a
    a/=2
    x+=1
print(f"Сумма {s} при {x-1} слагаемых")