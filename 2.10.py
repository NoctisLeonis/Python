import math
x= float (input("Введите значение x"))
y=float (input("Введите значение y"))
numbers = [ x, y]
avarage=sum(numbers) / len(numbers)
print(f"Среднее арифмитическое:{avarage}")

import statistics
a= float (input("Введите значение a"))
b=float (input("Введите значение b"))
numbers = [a,b]
geometric_mean = statistics.geometric_mean (numbers)
print(f"Среднее геометрическое : {geometric_mean}")



