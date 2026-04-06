# Задача 11.3
import random

n = 15

# а) от 0 до 1
arr_a = [random.random() for _ in range(n)]
print(f"а) от 0 до 1: {[round(x, 3) for x in arr_a]}")

# б) от 22 до 23
arr_b = [22 + random.random() for _ in range(n)]
print(f"б) от 22 до 23: {[round(x, 3) for x in arr_b]}")

# в) от 0 до 10
arr_c = [random.random() * 10 for _ in range(n)]
print(f"в) от 0 до 10: {[round(x, 3) for x in arr_c]}")

# г) от -50 до 50
arr_d = [random.random() * 100 - 50 for _ in range(n)]
print(f"г) от -50 до 50: {[round(x, 3) for x in arr_d]}")

# д) целые от 0 до 10
arr_e = [random.randint(0, 10) for _ in range(n)]
print(f"д) целые от 0 до 10: {arr_e}")