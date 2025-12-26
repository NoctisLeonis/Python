number = int(input("Введите трехзначное число с различными цифрами: "))
digits = [number // 100, (number // 10) % 10, number % 10]

# Все возможные перестановки
permutations = [
    digits[0] * 100 + digits[1] * 10 + digits[2],
    digits[0] * 100 + digits[2] * 10 + digits[1],
    digits[1] * 100 + digits[0] * 10 + digits[2],
    digits[1] * 100 + digits[2] * 10 + digits[0],
    digits[2] * 100 + digits[0] * 10 + digits[1],
    digits[2] * 100 + digits[1] * 10 + digits[0]
]

print("Числа, образованные перестановкой цифр:")
for num in permutations:
    print(num)
