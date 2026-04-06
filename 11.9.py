import random

arr = []
while len(arr) < 20:
    num = random.randint(1, 100)
    if num not in arr:
        arr.append(num)

print("Массив из неповторяющихся чисел:", arr)