k = int(input("Порог баллов? "))
a = int(input("Сколько набрал очков первый ученик? "))
b = int(input("Сколько набрал очков второй ученик? "))

if a>k and b>k:
    print("Оба ученика попали в команду")
elif a>k and b<k:
    print("Первый ученик попали в команду")
elif a<k and b>k:
    print("Второй ученик попали в команду")
else:
    print("Никто не попал в команду")