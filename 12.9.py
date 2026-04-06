matrix = [
    [10, 20, 30],
    [40, 50, 60],
    [70, 80, 90]
]
print("Массив:")
for row in matrix:
    print(row)

rows = len(matrix)
cols = len(matrix[0]) if rows > 0 else 0

if rows > 0 and cols > 0:
    # а) сумма левого верхнего и правого нижнего
    top_left = matrix[0][0]
    bottom_right = matrix[rows - 1][cols - 1]
    sum_corners = top_left + bottom_right
    print(f"\nа) Левый верхний ({top_left}) + Правый нижний ({bottom_right}) = {sum_corners}")

    # б) среднее арифметическое четырёх углов
    top_right = matrix[0][cols - 1]
    bottom_left = matrix[rows - 1][0]
    avg_corners = (top_left + top_right + bottom_left + bottom_right) / 4
    print(f"б) Среднее арифметическое четырёх углов: {avg_corners}")