# Создаём массив 6x6
matrix = [[i * 10 + j for j in range(1, 7)] for i in range(1, 7)]
print("Массив:")
for row in matrix:
    print(row)

# а) пятая строка (индекс 4)
if len(matrix) >= 5:
    print(f"а) Пятая строка: {matrix[4]}")

# б) s-й столбец
s = int(input("б) Введите номер столбца (1-6): "))
if 1 <= s <= len(matrix[0]):
    col = [matrix[i][s-1] for i in range(len(matrix))]
    print(f"Столбец {s}: {col}")