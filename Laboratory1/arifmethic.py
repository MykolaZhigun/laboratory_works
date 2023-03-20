def main():
    number1 = int(input("Введите первое число: "))
    number2 = int(input("Введите второе число: "))

    print("Введите число которое значит операцию (1. +; 2. -; 3. /; 4. *;)")
    operation = int(input("Число операции (1-4): "))
    print("_"*23)
    if 1 <= int(operation) <= 4:
        if int(operation) == 1:
            result = int(number1) + int(number2)
            print("Результат: " + str(number1) + " + " + str(number2) + " = " + str(result))
        elif int(operation) == 2:
            result = int(number1) - int(number2)
            print("Результат: " + str(number1) + " - " + str(number2) + " = " + str(result))
        elif int(operation) == 3:
            result = int(number1) / int(number2)
            print("Результат: " + str(number1) + " / " + str(number2) + " = " + str(result))
        elif int(operation) == 4:
            result = int(number1) * int(number2)
            print("Результат: " + str(number1) + " * " + str(number2) + " = " + str(result))
        pass
    else:
        print("#Введите число от 1 до 4#")


if __name__ == "__main__":
    main()
