number = int(input("Введите число n (n > 999): "))
hundreds = (number // 100) % 10
thousands = (number // 1000) % 10
print("Число сотен:", hundreds)
print("Число тысяч:", thousands)