import math

matrix = [
    [-5, 2, 8],
    [4, -10, 6],
    [7, 1, -3]
]
print("Массив:")
for row in matrix:
    print(row)

rows = len(matrix)
cols = len(matrix[0]) if rows > 0 else 0

if rows > 0 and cols > 0:
    # а) сравнение верхнего правого с любым другим по модулю
    top_right = matrix[0][cols - 1]
    abs_top_right = abs(top_right)
    print(f"\nа) Верхний правый угол: {top_right}, |{top_right}| = {abs_top_right}")

    r = int(input("   Введите строку другого элемента: "))
    c = int(input("   Введите столбец другого элемента: "))
    if 0 <= r < rows and 0 <= c < cols:
        other = matrix[r][c]
        abs_other = abs(other)
        print(f"   Другой элемент: {other}, |{other}| = {abs_other}")
        if abs_top_right > abs_other:
            print(f"   |Верхний правый| ({abs_top_right}) больше")
        elif abs_top_right < abs_other:
            print(f"   |Другой элемент| ({abs_other}) больше")
        else:
            print("   Абсолютные величины равны")

    # б) сравнение двух любых элементов
    print("\nб) Сравнение двух любых элементов")
    r1 = int(input("   Первый элемент - номер строки: "))
    c1 = int(input("                номер столбца: "))
    r2 = int(input("   Второй элемент - номер строки: "))
    c2 = int(input("                номер столбца: "))

    if (0 <= r1 < rows and 0 <= c1 < cols and
        0 <= r2 < rows and 0 <= c2 < cols):
        elem1 = matrix[r1][c1]
        elem2 = matrix[r2][c2]
        print(f"   Первый элемент: {elem1}, Второй элемент: {elem2}")
        if elem1 < elem2:
            print(f"   Первый элемент ({elem1}) меньше")
        elif elem1 > elem2:
            print(f"   Второй элемент ({elem2}) меньше")
        else:
            print("   Элементы равны")