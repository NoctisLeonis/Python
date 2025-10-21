import math

def ring_area(R, r):
    return math.pi * (R ** 2 - r ** 2)

R = float(input("Введите внешний радиус кольца: "))
r = float(input("Введите внутренний радиус кольца: "))
area = ring_area(R, r)
print(f"Площадь кольца: {area:}")