class Person1:
    year = 0
    high = 0
    weight = 0


class Person2:
    year = 0
    high = 0
    weight = 0


def person1_more_information():
    Person1.year = int(input("Уведіть кількість років 1-шій людині: "))
    Person1.high = int(input("Уведіть зріст першої людині: "))
    Person1.weight = int(input("Уведіть вагу першої людині: "))


def person2_more_information():
    Person2.year = int(input("Уведіть кількість років 2-гій людині: "))
    Person2.high = int(input("Уведіть зріст другої людині: : "))
    Person2.weight = int(input("Введите вес другої человека: "))


def main():

    person1_more_information()
    print("_"*50)
    person2_more_information()
    print("_"*50)

    print("Зрівнюємо: \nРоки: ")
    if Person1.year > Person2.year:
        print(f"{Person1.year} > {Person2.year}")
    elif Person1.year < Person2.year:
        print(f"{Person1.year} < {Person2.year}")
    elif Person1.year == Person2.year:
        print(f"{Person1.year} = {Person2.year}")

    print("Зріст: ")
    if Person1.high > Person2.high:
        print(f"{Person1.high} > {Person2.high}")
    elif Person1.high < Person2.high:
        print(f"{Person1.high} < {Person2.high}")
    elif Person1.high == Person2.high:
        print(f"{Person1.high} = {Person2.high}")

    print("Вага: ")
    if Person1.weight > Person2.weight:
        print(f"{Person1.weight} > {Person2.weight}")
    elif Person1.weight < Person2.weight:
        print(f"{Person1.weight} < {Person2.weight}")
    elif Person1.weight == Person2.weight:
        print(f"{Person1.weight} = {Person2.weight}")


if __name__ == '__main__':
    main()
