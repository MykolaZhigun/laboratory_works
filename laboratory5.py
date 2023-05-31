import requests


def authentication(login: str, password: str):
    response = requests.post("https://ksu24.kspu.edu/api/v2/login/",
                             data={'username': login, 'password': password})

    if response:
        print("\nВхід вдалий!\n")
    else:
        print("Помилка. Напевно ви неправильно ввели логін або пароль!")

    try:
        cookie = response.cookies.get_dict()["JWT"]
        return cookie
    except():
        print("Не правильно. Не можливо отримати кукі.")
        return


def get_value(url: str, cookie, key, filter_by: dict = None):
    response = requests.get(url=url, cookies={'JWT': cookie})
    response.raise_for_status()

    data = response.json()
    for item in data.get('results', [data]):
        if filter_by and item.get(list(filter_by.keys())[0]) != filter_by.get(list(filter_by.keys())[0]):
            continue
        if key in item:
            return item[key]

def information_student(url, cookie):
    response = requests.get(url=url, cookies={'JWT': cookie})
    response.raise_for_status()

    data = response.json()
    results_list = data.get('results', [data])
    for dictionary in results_list:
        for key, value in dictionary.items():
            print(f"{key}: {value}")
        print("-" * 50)

def main():
    login = input("Логін: ")
    password = input("Пароль: ")

    auth_student = authentication(login=login, password=password)
    print("Робимо запит на сервер...")
    print("-" * 50)
    information_student(url="https://ksu24.kspu.edu/api/v2/my/profile/", cookie=auth_student)

    print("Запит на отмання інформації про студента")
    information_student(url="https://ksu24.kspu.edu/api/v2/my/students/", cookie=auth_student)

main()
