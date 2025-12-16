number = int(input("Введите двузначное число: "))
reversed_number = number % 10 * 10 + number // 10
print(f"Число после перестановки цифр: {reversed_number}")
