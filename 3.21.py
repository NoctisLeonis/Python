number = int(input("Введите трехзначное число: "))
reversed_number = number % 10 * 100 + (number // 10) % 10 * 10 + number // 100
print(f"Число справа налево: {reversed_number}")
