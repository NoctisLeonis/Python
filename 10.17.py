def digit_count(n):
    if n == 0:
        return 1
    count = 0
    while n > 0:
        count += 1
        n //= 10
    return count

num1 = int(input("Введите первое число: "))
num2 = int(input("Введите второе число: "))

digits1 = digit_count(num1)
digits2 = digit_count(num2)

if digits1 > digits2:
    print(f"В первом числе ({num1}) больше цифр ({digits1})")
elif digits1 < digits2:
    print(f"Во втором числе ({num2}) больше цифр ({digits2})")
else:
    print(f"Количество цифр одинаковое: {digits1}")