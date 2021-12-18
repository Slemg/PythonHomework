number = int(input("Введите число:"))
multiplicity = int(input('На какое число хотим узнать кратность?:'))

if number % multiplicity == 0:
    print('Делится без остатка')
elif number % multiplicity > 0:
    print('Будет остаток')
