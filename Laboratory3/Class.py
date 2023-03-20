class Person:
    def __init__(self, year, high, weight):
        self.year = year
        self.high = high
        self.weight = weight

person1 = Person(17, 163, 81)
person2 = Person(13, 163, 82)

print("Порівнюємо вік: ")
if person1.year > person2.year:
    print(f"Вік першої персони {person1.year} більше ніж другої {person2.year}")
elif person1.year == person2.year:
    print(f"Вік однаковий. Вік першої персони {person1.year}. Вік другої персони: {person2.year}")
else:
    print(f"Вік першої персони {person1.year} меньше ніж другої {person2.year}")

print("\nПорівнюємо зріст: ")
if person1.high > person2.high:
    print(f"Зріст першої персони {person1.high} більше ніж другої {person2.high}")
elif person1.high == person2.high:
    print(f"Зріст однаковий. Зріст першої персони {person1.high}. Зріст другої персони: {person2.high}")
else:
    print(f"Зріст першої персони {person1.high} меньше ніж другої {person2.high}")

print("\nПорівнюємо вагу: ")
if person1.weight > person2.weight:
    print(f"Вага першої персони {person1.weight} більше ніж другої {person2.weight}")
elif person1.weight == person2.weight:
    print(f"Вага однакова. Вага першої персони {person1.weight}. Вага другої персони: {person2.weight}")
else:
    print(f"Вага першої персони {person1.weight} меньше ніж другої {person2.weight}")
