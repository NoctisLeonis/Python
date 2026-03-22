a = float(input("Введите первое число: "))
b = float(input("Введите второе число: "))

# Используем один условный оператор
if a > b:
    max_val = a
    min_val = b
else:
    max_val = b
    min_val = a

print(f"Максимальное значение: {max_val}")
print(f"Минимальное значение: {min_val}")