seat_number = int(input("Введите номер места: "))
compartment_number = (seat_number - 1) // 4 + 1
print(f"Место находится в купе №{compartment_number}.")
