arr = [10, 20, 30, 40, 50]
print("Исходный массив:", arr)

# а) увеличить в 2 раза
arr_double = [x * 2 for x in arr]
print(f"а) Увеличенный в 2 раза: {arr_double}")

# б) уменьшить на A
A = float(input("Введите A для уменьшения: "))
arr_sub = [x - A for x in arr]
print(f"б) Уменьшенный на {A}: {arr_sub}")

# в) разделить на первый элемент
if arr[0] != 0:
    arr_div = [x / arr[0] for x in arr]
    print(f"в) Разделённый на первый элемент ({arr[0]}): {[round(x, 3) for x in arr_div]}")
else:
    print("в) Невозможно: первый элемент равен 0")