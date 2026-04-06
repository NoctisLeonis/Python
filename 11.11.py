arr = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
print("Массив:", arr)
index = int(input("Введите индекс элемента (0-9): "))
if 0 <= index < len(arr):
    print(f"Элемент с индексом {index}: {arr[index]}")
else:
    print("Неверный индекс")