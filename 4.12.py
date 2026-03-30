import math

# 1. Вводим данные
r = float(input("Введите радиус круга: "))
a = float(input("Введите сторону квадрата: "))

# 2. Вычисляем площади
# math.pi дает более точное значение числа Пи
s_circle = math.pi * (r ** 2)
s_square = a ** 2

# 3. Сравниваем и выводим результат
if s_circle > s_square:
    print(f"Площадь круга ({s_circle:.2f}) больше площади квадрата ({s_square:.2f})")
elif s_square > s_circle:
    print(f"Площадь квадрата ({s_square:.2f}) больше площади круга ({s_circle:.2f})")
else:
    print("Площади фигур равны")
