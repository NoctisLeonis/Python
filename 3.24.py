number = int(input("Введите трехзначное число: "))
first_digit = number // 100
second_digit = (number // 10) % 10
third_digit = number % 10
new_number = second_digit * 100 + first_digit * 10 + third_digit
print(f"Число после перестановки первой и второй цифр: {new_number}")
