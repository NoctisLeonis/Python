import math

def is_perfect_square(x):
    if x < 0:
        return False
    root = int(math.sqrt(x))
    return root * root == x

n = int(input("Введите количество чисел n: "))
count = 0

for i in range(1, n + 1):
    a = int(input(f"Введите a{i}: "))
    if is_perfect_square(a):
        count += 1

print(f"Количество полных квадратов: {count}")