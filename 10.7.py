import math
def distance(x1, y1, x2, y2):
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
print("Введите координаты вершин треугольника:")
x1 = float(input("  x1 = "))
y1 = float(input("  y1 = "))
x2 = float(input("  x2 = "))
y2 = float(input("  y2 = "))
x3 = float(input("  x3 = "))
y3 = float(input("  y3 = "))
a = distance(x1, y1, x2, y2)
b = distance(x2, y2, x3, y3)
c = distance(x3, y3, x1, y1)
perimeter = a + b + c
print(f"Периметр треугольника: {perimeter:.2f}")