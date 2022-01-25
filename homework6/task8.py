s = int(input("Какой вклад хотите внести? "))
n = int(input("Какой процент годовых вы хотите? "))
a = 0

while n+1 > a:
    k = s/100*n
    s = s+k
    a = a+1
    print(s)
