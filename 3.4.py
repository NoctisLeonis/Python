N = int(input("Введите количество школьников: "))
k = int(input("Введите количество яблок: "))
apples_per_student = k // N
apples_left = k % N
print(f"Каждому школьнику достанется {apples_per_student} яблок, в корзинке останется {apples_left}.")
