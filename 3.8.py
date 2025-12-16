ticket_number = int(input("Введите серийный номер билета: "))
row = (ticket_number - 1643) // 15 + 1
print(f"Место находится в {row} ряду.")
