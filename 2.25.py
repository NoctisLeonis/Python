def parallelepiped(a, b, c):
    volume = a * b * c
    side_area = 2 * (a + b) * c
    return volume, side_area
a = float(input("Введите длину первой стороны: "))
b = float(input("Введите длину второй стороны: "))
c = float(input("Введите длину третьей стороны: "))
vol, area = parallelepiped(a, b, c)

print(f"Объём параллелепипеда: {vol:}")
print(f"Площадь боковой поверхности: {area: }")