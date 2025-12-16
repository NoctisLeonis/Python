place_number = int(input("Введите номер места: "))
shelf = (place_number - 1) // 120 + 1  # Ярус
section = ((place_number - 1) % 120) // 15 + 1  # Секция
print(f"Товар находится на {shelf} ярусе, в {section} секции.")
