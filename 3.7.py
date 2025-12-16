apartment_number = int(input("Введите номер квартиры: "))
floor = (apartment_number - 1) // 3 + 1
print(f"Квартира находится на {floor} этаже.")
