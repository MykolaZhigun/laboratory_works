# -*- coding: utf-8 -*-

def main():
    number1 = int(input("Введите первое число: "))
    number2 = int(input("Введите второе число: "))

    print("Введите число которое соответсвует операции (1. +; 2. -; 3. /; 4. *;)")
    operation = int(input("Число операции (1-4): "))
    print("_"*23)
    if 1 <= operation <= 4:
        if operation == 1:
            print(f"Результат: {number1} + {number2} = {number1 + number2}")
        elif operation == 2:
            print(f"Результат: {number1} - {number2} = {number1 - number2}")
        elif operation == 3:
            print(f"Результат: {number1} / {number2} = {number1 / number2}")
        else:
            print(f"Результат: {number1} * {number2} = {number1 * number2}")
    else:
        print("# Вам нужно было ввести число от 1 до 4 #")


if __name__ == "__main__":
    main()
