def factorial(n):
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result

numerator = 2 * factorial(5) + 3 * factorial(8)
denominator = factorial(6) + factorial(4)
value = numerator / denominator

print(f"2·5! + 3·8! = {numerator}")
print(f"6! + 4! = {denominator}")
print(f"Результат: {value:.4f}")