import math
x= float (input("Введите длину первого катета x"))
y=float (input("Введите длину первого катета y"))
a= math.sqrt(x**2)+(y**2)
perimetr = x+y+a
print(f"Длина гипотенузы (a): {a}")
print(f"Периметр треугольника :{perimetr}")