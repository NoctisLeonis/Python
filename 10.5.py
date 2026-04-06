import math

def trapezoid_perimeter(a, b, h):
    """
    a, b - основания (a >= b)
    h - высота
    """
    side = math.sqrt(((a - b) / 2) ** 2 + h ** 2)
    return a + b + 2 * side

print("Первая трапеция:")
a1 = float(input("  Введите большее основание: "))
b1 = float(input("  Введите меньшее основание: "))
h1 = float(input("  Введите высоту: "))

print("Вторая трапеция:")
a2 = float(input("  Введите большее основание: "))
b2 = float(input("  Введите меньшее основание: "))
h2 = float(input("  Введите высоту: "))

perimeter_sum = trapezoid_perimeter(a1, b1, h1) + trapezoid_perimeter(a2, b2, h2)
print(f"Сумма периметров: {perimeter_sum:.2f}")