import math

def trapeze_perimeter(a, b, h):
    c = math.sqrt(h**2 + ((a - b)/2)**2)
    return a + b + 2 * c
a = float(input("Введите длину большего основания: "))
b = float(input("Введите длину меньшего основания: "))
h = float(input("Введите высоту трапеции: "))
perimeter = trapeze_perimeter(a, b, h)
print(f"Периметр трапеции: {perimeter:}")