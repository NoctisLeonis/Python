apartment_number = int(input("Введите номер квартиры: "))
apartments_per_entrance = 9 * 6  # 54 квартиры в подъезде
entrance = (apartment_number - 1) // apartments_per_entrance + 1
floor_in_entrance = ((apartment_number - 1) % apartments_per_entrance) // 6 + 1
position_on_floor = ((apartment_number - 1) % apartments_per_entrance) % 6 + 1
print(f"Квартира находится в {entrance} подъезде, на {floor_in_entrance} этаже, {position_on_floor}-я на этаже.")
