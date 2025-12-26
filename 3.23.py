number = int(input("Введите трехзначное число: "))
last_digit = number % 10
remaining = number // 10
new_number = last_digit * 100 + remaining
print(f"Полученное число: {new_number}")
