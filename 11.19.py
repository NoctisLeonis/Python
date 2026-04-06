# Создаём пример двумерного массива 3x3
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

rows = len(matrix)
cols = len(matrix[0]) if rows > 0 else 0

# а) правый верхний угол
if rows > 0 and cols > 0:
    top_right = matrix[0][cols - 1]
    print(f"а) Правый верхний угол: {top_right}")

# б) левый нижний угол
if rows > 0 and cols > 0:
    bottom_left = matrix[rows - 1][0]
    print(f"б) Левый нижний угол: {bottom_left}")