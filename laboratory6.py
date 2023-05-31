import requests
import pandas as pd
import matplotlib.pyplot as plt


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


def get_value(url: str, auth_cookie, key, filter_by: dict = None):
    response = requests.get(url=url, cookies={'JWT': auth_cookie})
    response.raise_for_status()

    data = response.json()
    for item in data.get('results', [data]):
        if filter_by and item.get(list(filter_by.keys())[0]) != filter_by.get(list(filter_by.keys())[0]):
            continue
        if key in item:
            return item[key]

def information_student(url, auth_cookie):
    response = requests.get(url=url, cookies={'JWT': auth_cookie})
    response.raise_for_status()

    data = response.json()
    results_list = data.get('results', [data])
    for dictionary in results_list:
        for key, value in dictionary.items():
            print(f"{key}: {value}")
        print("-" * 50)

def get_json(url: str, auth_cookie):
    profile_request = requests.get(url=url, cookies={'JWT': auth_cookie})

    if profile_request.ok:
        print("Запит виконано!")
        return profile_request.json()
    else:
        print(f"Помилка під час отримання запиту. Кoд:{profile_request.status_code}")
        profile_request.raise_for_status()
        return None

def create_graphic(df: pd.DataFrame, key):
    try:
        df[key].plot(kind="barh", title='Графік балів студента.')
        plt.show()
    except():
        print("Помилка.")

def sort_data_frame(df, colums, inplance=True, ascending=False, ignore_index=False, key=None):
    return df.sort_values(by=colums, inplace=inplance, ascending=ascending, ignore_index=ignore_index, key=key)




def main():
    login = input("Логін: ")
    password = input("Пароль: ")

    auth_cookie = authentication(login=login, password=password)

    student_id = get_value(url="https://ksu24.kspu.edu/api/v2/my/students/", auth_cookie=auth_cookie, key="id")

    print("Запит на отмання журнала...")
    information_student(url="https://ksu24.kspu.edu/api/v2/my/students/" + str(student_id) + "/recordbooks/", auth_cookie=auth_cookie)
    recordbook_id = get_value(url="https://ksu24.kspu.edu/api/v2/my/students/" + str(student_id) + "/recordbooks/",
                              auth_cookie=auth_cookie, key="id")

    print("Чекаємо відповідь на запит про отримання оцінок для дисциплін")
    information_student(
        url="https://ksu24.kspu.edu/api/v2/my/students/" + student_id + "/recordbooks/" + recordbook_id + "/records",
        auth_cookie=auth_cookie)

    data = get_json(
        url="https://ksu24.kspu.edu/api/v2/my/students/" + student_id + "/recordbooks/" + recordbook_id + "/records",
        auth_cookie=auth_cookie)

    if "results" in data.keys():
        results_list = data["results"]
        df = pd.DataFrame.from_records(results_list)
    else:
        df = pd.DataFrame(data)

    sort_data_frame(df, ["result"], ascending=True)
    df.to_excel("test1.xlsx", sheet_name="Оцінки_Студента", index=False)
    create_graphic(df, "result")


main()
