word = input("Введите слово: ")
if len(word) >= 3:
    print(f"Третий символ: {word[2]}")
else:
    print("Слово слишком короткое")