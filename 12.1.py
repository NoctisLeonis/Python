matrix = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12]
]

print("Массив:")
for row in matrix:
    print(row)

# а) любой элемент второй строки (индекс 1)
row_2 = matrix[1]
col = int(input("а) Введите номер столбца (0-3) для элемента второй строки: "))
if 0 <= col < len(row_2):
    print(f"Элемент во второй строке, столбец {col}: {row_2[col]}")

# б) любой элемент массива
r = int(input("б) Введите номер строки: "))
c = int(input("   Введите номер столбца: "))
if 0 <= r < len(matrix) and 0 <= c < len(matrix[0]):
    print(f"Элемент [{r}][{c}]: {matrix[r][c]}")