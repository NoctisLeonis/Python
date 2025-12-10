def caltulator ():
    print("Калькулятор")
    print("Доступные операции: +,-, *,/")
    try:
        num1 = float (input ("Введите первое число:"))
        operation = input("Введите операцию (+,-,*,/): ")
        num2 = float (input ("Введите второе число: "))

        if operation == '+':
             result = num1 + num2
             print (f"Результат: {num1}+ {num2} = {result}")
        elif operation == '-':
             result = num1 - num2
             print (f"Результат: {num1} - {num2} = {result}")
        elif operation == '*':
             print(f"Результат: {num1} * {num2} = {result}")
        elif operation == '/':
             if num2 != 0:
              result = num1/num2
              print(f"Результат: {num1} / {num2} = {result}")
             else:
              print("Ошибка: деления на ноль!")
        else:
              print("Ошибка: неверная операция!")
    except ValueError:
          print("Ошибка: введите корректное число!")
caltulator()






