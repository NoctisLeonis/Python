number = int(input("Введите число n (n > 99): "))
tens = (number // 10) % 10
hundreds = (number // 100) % 10
print("Число десятков:", tens)
print("Число сотен:", hundreds)