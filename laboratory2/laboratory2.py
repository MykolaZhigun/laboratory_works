def main():
    exp_var = ""
    exp_dictionary = {"1": "Привет ",
                      "2": "Мир",
                      "3": "!"}
    var_massive = [1,2,4,16,2,187] #массив для зрівняння далі
    exp_cortage = (1,2,5,16,2,187) #кортеж


    #Выводим текст 'Привет Мир!' с помощью классов
    for key_values in exp_dictionary.values():
        #Як працюють змінні
        exp_var += key_values

    print(exp_var)
    print("_"*20)

    print(f"{var_massive}: - Массив")
    print(f"{exp_cortage}: - Кортеж")

if __name__ == '__main__':
    main()