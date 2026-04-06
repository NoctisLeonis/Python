matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
print("Исходный массив:")
for row in matrix:
    print(row)

rows = len(matrix)
cols = len(matrix[0]) if rows > 0 else 0

if rows > 0 and cols > 0:
    # а) правый верхний и левый нижний
    temp = matrix[0][cols - 1]
    matrix[0][cols - 1] = matrix[rows - 1][0]
    matrix[rows - 1][0] = temp
    print("\nа) После обмена правого верхнего и левого нижнего:")
    for row in matrix:
        print(row)

# Восстанавливаем исходный массив для пункта б
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

if rows > 0 and cols > 0:
    # б) правый нижний и левый верхний
    temp = matrix[0][0]
    matrix[0][0] = matrix[rows - 1][cols - 1]
    matrix[rows - 1][cols - 1] = temp
    print("\nб) После обмена правого нижнего и левого верхнего:")
    for row in matrix:
        print(row)