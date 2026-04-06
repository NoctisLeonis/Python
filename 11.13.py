import math

arr = [4, 9, 16, 25, 36, 49, 64, 81, 100]
print("Массив:", arr)

# а)
index = int(input("Введите индекс элемента для извлечения корня: "))
if 0 <= index < len(arr):
    print(f"Корень из arr[{index}] = {arr[index]} = {math.sqrt(arr[index]):.2f}")

# б)
i1 = int(input("Введите индекс первого элемента: "))
i2 = int(input("Введите индекс второго элемента: "))
if 0 <= i1 < len(arr) and 0 <= i2 < len(arr):
    avg = (arr[i1] + arr[i2]) / 2
    print(f"Среднее арифметическое arr[{i1}] и arr[{i2}]: {avg}")