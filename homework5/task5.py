s = 0
x = 1 
print("S = 1 + 3 + 5 + 7 + 9 + ....... + n")
n = int(input("Введитe n: "))
for x in range(1, n+1, 2):  
        print(f"Слагаемое {x}")
        s+=x
print(f"Сумма {s} для числа {n}")