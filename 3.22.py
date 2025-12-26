number = int(input("Введите трехзначное число: "))
first_digit = number // 100
remaining = number % 100
new_number = remaining * 10 + first_digit
print(f"Полученное число: {new_number}")
