n = float(input("Введите число n: "))
if n <= 0:
    print("Ошибка: n должно быть положительным")
else:
    k = 1
    total = 0.0

    while total <= n:
        total += 1 / k
        print(f"H_{k} = {total:.6f}")
        k += 1
    print(f"\nПервая гармоническая сумма, большая {n}: H_{k - 1} = {total:.6f}")