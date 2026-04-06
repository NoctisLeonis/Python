matrix = [
    [8, 2, 3],
    [4, 5, 6],
    [7, 1, 9]
]
print("Массив:")
for row in matrix:
    print(row)

rows = len(matrix)
cols = len(matrix[0]) if rows > 0 else 0

if rows > 0 and cols > 0:
    # а) правый нижний vs левый нижний
    bottom_right = matrix[rows - 1][cols - 1]
    bottom_left = matrix[rows - 1][0]
    print(f"\nа) Правый нижний: {bottom_right}, Левый нижний: {bottom_left}")
    if bottom_right < bottom_left:
        print(f"   Правый нижний ({bottom_right}) меньше")
    elif bottom_right > bottom_left:
        print(f"   Левый нижний ({bottom_left}) меньше")
    else:
        print("   Они равны")

    # б) правый верхний vs левый нижний
    top_right = matrix[0][cols - 1]
    print(f"б) Правый верхний: {top_right}, Левый нижний: {bottom_left}")
    if top_right < bottom_left:
        print(f"   Правый верхний ({top_right}) меньше")
    elif top_right > bottom_left:
        print(f"   Левый нижний ({bottom_left}) меньше")
    else:
        print("   Они равны")