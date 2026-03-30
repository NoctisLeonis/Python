import math
s_circle = float(input("Введите площадь круга: "))
s_square = float(input("Введите площадь квадрата: "))
# Находим характерные размеры
radius = math.sqrt(s_circle / math.pi)
diameter = 2 * radius
side = math.sqrt(s_square)
diagonal = side * math.sqrt(2)
# а) Уместится ли круг в квадрате?
# Круг влезет, если его диаметр не больше стороны квадрата
if diameter <= side:
    print("Круг поместится в квадрате")
else:
    print("Круг НЕ поместится в квадрате")
# б) Уместится ли квадрат в круге?
# Квадрат влезет, если его диагональ не больше диаметра круга
if diagonal <= diameter:
    print("Квадрат поместится в круге")
else:
    print("Квадрат НЕ поместится в круге")
