def find_floor(apartment_number):
    apartments_per_floor = 3
    floors = 5
    if apartment_number < 1 or apartment_number > 15:
        return "Некорректный номер квартиры"
    floor = (apartment_number - 1) // apartments_per_floor + 1
    return floor

apartment = int(input("Введите номер квартиры: "))
print(f"Квартира находится на {find_floor(apartment)} этаже.")
