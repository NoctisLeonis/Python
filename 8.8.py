# Ввод значения a
a = float(input("Введите a (1 < a <= 1.5): "))
# Проверка допустимости a
if not (1 < a <= 1.5):
    print("Ошибка: a должно быть в интервале (1, 1.5]")
else:
    print(f"\nЗначения n, при которых 1 + 1/n >= {a}:")
    n = 2
    while True:
        value = 1 + 1/n
        if value < a:
            break
        print(f"n = {n}  (1 + 1/{n} = {value:.4f})")
        n += 1