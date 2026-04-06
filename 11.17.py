arr = [3, 5, 7, 2, 8, 4, 6, 9, 1, 10]
print("Массив:", arr)

# а) сумма всех элементов
total_sum = sum(arr)
print(f"а) Сумма всех элементов: {total_sum}")

# б) произведение всех элементов
product = 1
for x in arr:
    product *= x
print(f"б) Произведение всех элементов: {product}")

# в) сумма квадратов
sum_sq = sum(x**2 for x in arr)
print(f"в) Сумма квадратов: {sum_sq}")

# г) сумма шести первых элементов
sum_first6 = sum(arr[:6])
print(f"г) Сумма первых 6 элементов: {sum_first6}")

# д) сумма с k1 по k2
k1 = int(input("Введите k1 (индекс, 0-9): "))
k2 = int(input("Введите k2 (индекс, k2 > k1): "))
if 0 <= k1 < k2 < len(arr):
    sum_range = sum(arr[k1:k2+1])
    print(f"д) Сумма с {k1} по {k2}: {sum_range}")

# е) среднее арифметическое всех элементов
avg_all = total_sum / len(arr)
print(f"е) Среднее арифметическое всех элементов: {avg_all:.2f}")

# ж) среднее арифметическое с s1 по s2
s1 = int(input("Введите s1 (индекс, 0-9): "))
s2 = int(input("Введите s2 (индекс, s2 > s1): "))
if 0 <= s1 < s2 < len(arr):
    avg_range = sum(arr[s1:s2+1]) / (s2 - s1 + 1)
    print(f"ж) Среднее арифметическое с {s1} по {s2}: {avg_range:.2f}")