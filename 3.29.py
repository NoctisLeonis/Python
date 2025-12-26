number = int(input("Введите число n (n > 9): "))
units = number % 10
tens = (number // 10) % 10
print("Число единиц:", units)
print("Число десятков:", tens)