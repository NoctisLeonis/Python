a = float(input("Введите a (1 < a <= 1.5): "))
if not (1 < a <= 1.5):
    print("Ошибка: a должно быть в интервале (1, 1.5]")
else:
    n = 2
    while True:
        if 1 + 1/n < a:
            print(f"Наименьшее n: {n}")
            print(f"1 + 1/{n} = {1 + 1/n:.4f} < {a}")
            break
        n += 1