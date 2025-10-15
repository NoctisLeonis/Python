import math
x= float (input("Введите значение x"))
y=float (input("Введите значение y"))
if x == 0:
    print("Коэффициент 'x' не может быть равен 0.")
else:
    a= - y/x
    print(f"При a =", a, " значение функции y= ", y)
