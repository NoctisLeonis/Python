surname1 = input("Введите первую фамилию: ")
surname2 = input("Введите вторую фамилию: ")

if len(surname1) > len(surname2):
    print(f"Фамилия {surname1} длиннее")
elif len(surname1) < len(surname2):
    print(f"Фамилия {surname2} длиннее")
else:
    print("Фамилии одинаковой длины")