number = int(input("Введите трехзначное число: "))
first_digit = number // 100
second_digit = (number // 10) % 10
third_digit = number % 10
new_number = first_digit * 100 + third_digit * 10 + second_digit
print(f"Число после перестановки второй и третьей цифр: {new_number}")
