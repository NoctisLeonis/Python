import math

def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0:
            return False
    return True

primes = []
for num in range(100, 1000):
    if is_prime(num):
        primes.append(num)

print(f"Трёхзначные простые числа (всего {len(primes)}):")
print(primes)