number = int(input("Введите трехзначное число: "))
units = number % 10
tens = (number // 10) % 10
hundreds = number // 100
sum_digits = hundreds + tens + units
product_digits = hundreds * tens * units
print(f"Число единиц: {units}")
print(f"Число десятков: {tens}")
print(f"Сумма цифр: {sum_digits}")
print(f"Произведение цифр: {product_digits}")
