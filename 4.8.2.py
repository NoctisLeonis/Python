import math

x = float(input("Введите значение x: "))

# Вычисление k
if math.sin(x) >= 0:
    k = x ** 2
else:
    k = abs(x)

# Вычисление f
if x < k:
    f = abs(x)
else:
    f = k * x

print(f"f = {f}")