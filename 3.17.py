number = int(input("Введите двузначное число: "))
tens = number // 10
units = number % 10
sum_digits = tens + units
print(f"Сумма цифр: {sum_digits}")
