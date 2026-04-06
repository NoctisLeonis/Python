matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
print("Массив:")
for row in matrix:
    print(row)

# а) сумма двух любых элементов
print("\nа) Сумма двух любых элементов")
r1 = int(input("  Первый элемент - номер строки: "))
c1 = int(input("                номер столбца: "))
r2 = int(input("  Второй элемент - номер строки: "))
c2 = int(input("                номер столбца: "))

if (0 <= r1 < len(matrix) and 0 <= c1 < len(matrix[0]) and
    0 <= r2 < len(matrix) and 0 <= c2 < len(matrix[0])):
    sum_two = matrix[r1][c1] + matrix[r2][c2]
    print(f"  Сумма: {matrix[r1][c1]} + {matrix[r2][c2]} = {sum_two}")

# б) среднее арифметическое трёх любых элементов
print("\nб) Среднее арифметическое трёх любых элементов")
elements = []
for i in range(1, 4):
    r = int(input(f"  Элемент {i} - номер строки: "))
    c = int(input(f"           номер столбца: "))
    if 0 <= r < len(matrix) and 0 <= c < len(matrix[0]):
        elements.append(matrix[r][c])

if len(elements) == 3:
    avg_three = sum(elements) / 3
    print(f"  Среднее арифметическое: {avg_three}")