a = float(input("Введите a: "))
b = float(input("Введите b: "))
max1 = a if a > 2*b else 2*b
max2 = (2*a - b) if (2*a - b) > b else b
z1 = max1 * max2
print(f"Способ 1 (без функции): z = {z1:.2f}")
