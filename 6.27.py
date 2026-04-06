# Левая граница интервала
left = 100
# Находим первое число >= left, которое делится на 19
# Для этого можно поделить left на 19 и округлить вверх
if left % 19 == 0:
    first = left
else:
    first = left + (19 - left % 19)
print(f"Первое число >= {left}, кратное 19: {first}")
print()
# Выводим 15 первых чисел
count = 0
number = first

while count < 15:
    print(number)
    number = number + 19  # следующее кратное 19
    count = count + 1