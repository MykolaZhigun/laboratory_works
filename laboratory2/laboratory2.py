# -*- coding: utf-8 -*-

def main():
    exp_dictionary = {"1" : "Привіт ",
                      "2" : "Світ",
                      "3" : "!"}
    var_massive = [1, 2, 4, 16, 2, 187]  # массив 
    exp_cortage = (1, 2, 5, 16, 2, 187)  # кортеж


    # Збираємо значення зі словника в одну строку
    exp_var = ""
    for key_values in exp_dictionary.values():
        exp_var += key_values

    # Виводимо результати
    print(exp_var) 
    print("_"*20)
    print(f"{var_massive}: - Массив")
    print(f"{exp_cortage}: - Кортеж")

if __name__ == '__main__':
    main()
