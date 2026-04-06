a = float(input("Введите a (1 < a <= 1.5): "))
if not (1 < a <= 1.5):
    print("Ошибка: a должно быть в интервале (1, 1.5]")
else:
    n = 2
    print(f"\nЧисла 1 + 1/n, не меньшие {a}:")
    while True:
        value = 1 + 1/n
        if value < a:
            break
        print(f"1 + 1/{n} = {value:.4f}")
        n += 1