side1 = int(input("Введите сторону: "))
side2 = int(input("Введите сторону: "))
side3 = int(input("Введите сторону: "))
if side1 < side2 + side3 and side1**2 == side2**2 + side3**2:
    print("Треугольник существует,он прямоугольный")
elif side2 < side3 + side1 and side2**2 == side3**2 + side1**2:
    print("Треугольник существует,он прямоугольный")
elif side3 < side2 + side1 and side3**2 == side1**2 + side2**2:
    print("Треугольник существует,он прямоугольный")
else:
    print("Треугольник не соотвествует требованиям!")