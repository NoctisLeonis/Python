
n = int(input("Введите натуральное число: "))
number = n
# Начинаем с первой цифры
max_digit = number % 10
min_digit = number % 10
number = number // 10

# Проходим по остальным цифрам
while number > 0:
    digit = number % 10  # берём последнюю цифру
    if digit > max_digit:
        max_digit = digit
    if digit < min_digit:
        min_digit = digit
    number = number // 10  # отбрасываем последнюю цифру
print(f"Число: {n}")
print(f"а) Максимальная цифра: {max_digit}")
print(f"   Минимальная цифра: {min_digit}")
print(f"б) Разность (макс - мин): {max_digit - min_digit}")
print(f"в) Сумма (макс + мин): {max_digit + min_digit}")