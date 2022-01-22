side1 = int(input("Введите сторону: "))
side2 = int(input("Введите сторону: "))
side3 = int(input("Введите сторону: "))
if side1 < side2 + side3 and side1 == side3:
    print("Треугольник существует,он равнобедренный")
elif side2 < side3 + side1 and side2 == side3:
    print("Треугольник существует,он равнобедренный")
elif side3 < side2 + side1 and side1 == side2:
    print("Треугольник существует,он равнобедренный")
else:
    print("Треугольник не соотвествует требованиям!")