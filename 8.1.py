n = int(input("Введите число n: "))
print(f"\nНатуральные числа, квадраты которых ≤ {n}:")
print("=" * 40)
k = 1
count = 0
print("Проверяем числа по порядку:")
print("-" * 40)

while k * k <= n:
    print(f"  {k}² = {k*k} → не превышает {n}")
    count += 1
    k += 1
print("-" * 40)
print(f"Всего найдено чисел: {count}")