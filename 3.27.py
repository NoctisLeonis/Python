number = int(input("Введите 4-значное число: "))
a = number // 1000
b = (number // 100) % 10
c = (number // 10) % 10
d = number % 10
summa = a + b + c + d
print("Сумма цифр:", summa)
number = int(input("Введите 5-значное число: "))
a = number // 10000
b = (number // 1000) % 10
c = (number // 100) % 10
d = (number // 10) % 10
e = number % 10
summa = a + b + c + d + e
print("Сумма цифр:", summa)

