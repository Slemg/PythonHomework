i = 1
x = 10 
print("Подсчитать количество цифр в записи целого положительного числа.")
n = int(input("Введите число: "))
if n > 0:
    while n > x:
        i+=1
        x*=10           
    print(f"Количество цифр в записи целого положительного числа ---> {i}")    
else:
    print('Число отрицательное либо 0!')


# i = 0
# print("Подсчитать количество цифр в записи целого положительного числа.")
# n = int(input("Введите число: "))
# while n > 0:
#     n //=10 
#     i+=1      
# print(f"Количество цифр в записи целого положительного числа ---> {i}") 

# n = int(input("Введите число: "))
# k = len(str(n))
# print(k)

# i = 0
# print("Подсчитать количество цифр в записи целого положительного числа.")
# n = int(input("Введите число: "))
# while n > 1:
#     i+=1
#     n/=10
# print(f"Количество цифр в записи целого положительного числа ---> {i}")   