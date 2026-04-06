import math

def triangle_area(x1, y1, x2, y2, x3, y3):
    """Площадь треугольника по координатам вершин (формула Гаусса)"""
    return abs((x1*(y2 - y3) + x2*(y3 - y1) + x3*(y1 - y2)) / 2)

coords = []
for i in range(1, 6):
    x = float(input(f"x{i} = "))
    y = float(input(f"y{i} = "))
    coords.append((x, y))

area = 0
for i in range(1, 4):
    area += triangle_area(
        coords[0][0], coords[0][1],
        coords[i][0], coords[i][1],
        coords[i+1][0], coords[i+1][1]
    )

print(f"Площадь пятиугольника: {area:.2f}")