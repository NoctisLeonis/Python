number = int(input("Введите трехзначное число: "))
hundreds = number // 100
tens = (number // 10) % 10
units = number % 10
print(f"Цифры числа: {hundreds}, {tens}, {units}")
