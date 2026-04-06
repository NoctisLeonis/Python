word = input("Введите слово: ")
k = int(input("Введите номер символа (k): "))
if 1 <= k <= len(word):
    print(f"{k}-й символ: {word[k-1]}")
else:
    print("Некорректный номер символа")