a = float(input("Введите a (1 < a <= 1.5): "))

if not (1 < a <= 1.5):
    print("Ошибка: a должно быть в интервале (1, 1.5]")
else:
    n = 2
    while True:
        value = 1 + 1/n
        if value < a:
            print(f"Первое число, меньшее {a}: 1 + 1/{n} = {value:.4f}")
            break
        n += 1