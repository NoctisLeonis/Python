word = input("Введите слово: ")
if len(word) >= 4:
    result = word[1] + word[3]
    print(f"Буквосочетание из 2-го и 4-го символов: {result}")
else:
    print("Слово слишком короткое (нужно минимум 4 символа)")