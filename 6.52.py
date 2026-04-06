n = int(input("Введите натуральное число: "))
print(f"\nАнализируем число: {n}")
print("=" * 40)
number = n
has_three = False
has_two = False
has_five = False
# Один цикл для всех проверок
while number > 0:
    digit = number % 10
    if digit == 3:
        has_three = True
    if digit == 2:
        has_two = True
    if digit == 5:
        has_five = True
    number //= 10
# Вывод результатов
print("а)", end=" ")
if has_three:
    print("Да, цифра 3 есть в числе")
else:
    print("Нет, цифры 3 нет в числе")
print("б)", end=" ")
if has_two and has_five:
    print("Да, цифры 2 и 5 обе есть в числе")
else:
    print("Нет, цифры 2 и 5 не встречаются вместе")