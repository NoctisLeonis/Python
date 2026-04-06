x = float(input("Введите x: "))
y = float(input("Введите y: "))

def sign_without_func(a):
    if a < 0:
        return -1
    elif a == 0:
        return 0
    else:
        return 1

z1 = sign_without_func(x) + sign_without_func(y)
print(f"Способ 1 (без функции): z = {z1}")
