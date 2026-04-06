n = int(input("Введите натуральное число: "))
number = n
position = 1
result = 0
while number > 0:
    digit = number % 10  # берём последнюю цифру
    if digit == 8:
        result = position  # запоминаем позицию (чем дальше, тем больше номер)
    number = number // 10  # отбрасываем последнюю цифру
    position = position + 1  # увеличиваем позицию для следующей цифры
print(result)