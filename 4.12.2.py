import math

# Ввод данных
r = float(input("Введите радиус круга: "))
a = float(input("Введите сторону квадрата: "))

# Вычисление площадей
circle_area = math.pi * r ** 2
square_area = a ** 2

# Сравнение площадей
if circle_area > square_area:
    print(f"Площадь круга ({circle_area:.2f}) больше площади квадрата ({square_area:.2f})")
elif circle_area < square_area:
    print(f"Площадь квадрата ({square_area:.2f}) больше площади круга ({circle_area:.2f})")
else:
    print(f"Площади равны: {circle_area:.2f}")