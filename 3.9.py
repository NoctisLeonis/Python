n = int(input("Введите количество секунд: "))
hours = n // 3600
remaining_seconds = n % 3600
minutes = remaining_seconds // 60
seconds = remaining_seconds % 60

print(f"Полных часов: {hours}")
print(f"Полных минут с начала часа: {minutes}")
print(f"Полных секунд с начала минуты: {seconds}")
