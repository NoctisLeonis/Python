matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12], [13, 14, 15]]
print("Исходный массив:")
for row in matrix:
    print(row)

# а) замена элемента пятой строки (индекс 4)
if len(matrix) >= 5:
    col = int(input("а) Введите номер столбца (0-2) в пятой строке: "))
    if 0 <= col < len(matrix[4]):
        matrix[4][col] = 1949
        print(f"После замены в пятой строке:")
        for row in matrix:
            print(row)

# б) замена любого элемента числом a
a = int(input("б) Введите число a: "))
r = int(input("   Введите номер строки: "))
c = int(input("   Введите номер столбца: "))
if 0 <= r < len(matrix) and 0 <= c < len(matrix[0]):
    matrix[r][c] = a
    print("После замены:")
    for row in matrix:
        print(row)