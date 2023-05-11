# coding: utf8

new_file = open("value_person.txt", "w")
number_person = 1


class Person:

    def __init__(self, year, high, weight):
        global number_person

        self.year = year
        self.high = high
        self.weight = weight

        if number_person == 1:
            new_file.write("Інформація першої людини:\n")
        elif number_person == 2:
            new_file.write("\nІнформація другої людини:\n")
        number_person += 1
        new_file.write(f"Кількість років людини: {self.year}\n")
        new_file.write(f"Зріст людини: {self.high}\n")
        new_file.write(f"Вага людини: {self.weight}\n")


person1 = Person(17, 163, 81)
person2 = Person(13, 163, 82)

if person1.year > person2.year:
    new_file.write(f"\nВік першої персони {person1.year} більше ніж другої {person2.year}")
elif person1.year == person2.year:
    new_file.write(f"\nВік однаковий. Вік першої персони {person1.year}. Вік другої персони: {person2.year}")
else:
    new_file.write(f"\nВік першої персони {person1.year} меньше ніж другої {person2.year}")

if person1.high > person2.high:
    new_file.write(f"\nЗріст першої персони {person1.high} більше ніж другої {person2.high}")
elif person1.high == person2.high:
    new_file.write(f"\nЗріст однаковий. Зріст першої персони {person1.high}. Зріст другої персони: {person2.high}")
else:
    new_file.write(f"\nЗріст першої персони {person1.high} меньше ніж другої {person2.high}")

if person1.weight > person2.weight:
    new_file.write(f"\nВага першої персони {person1.weight} більше ніж другої {person2.weight}")
elif person1.weight == person2.weight:
    new_file.write(f"\nВага однакова. Вага першої персони {person1.weight}. Вага другої персони: {person2.weight}")
else:
    new_file.write(f"\nВага першої персони {person1.weight} меньше ніж другої {person2.weight}")

new_file.close()
