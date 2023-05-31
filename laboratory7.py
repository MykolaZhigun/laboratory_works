from flask import Flask
from flask import request
import requests

app = Flask(__name__)


def format_information(data: dict) -> str:
    page = f"""
        <html>
            <head>
                <title>{data['email']}</title>
            </head>
            <body>
                <h1>{data['surname']} {data['name']}</h1>
                <h2>{data['birthday']}</h2>
                <img src="{data['image']}">
            </body>
        </html>
    """
    return page


login_page = """
<form action="/" method="post">
  <label for="login">Логін:</label>
  <input type="text" id="login" name="login"><br><br>
  <label for="lname">Пароль:</label>
  <input type="password" id="password" name="password"><br><br>
  <input type="submit" value="Submit">
</form>"""


@app.route('/', methods=["POST"])
def have_information():
    login_incoming = request.form['login']
    password_incoming = request.form['password']

    auth = requests.post("https://ksu24.kspu.edu/api/v2/login/", data={
        'username': login_incoming,
        'password': password_incoming
    })
    response = requests.post("https://ksu24.kspu.edu/api/v2/login/",
                             data={'username': login_incoming, 'password': password_incoming})

    if response:
        auth_cookie = auth.cookies.get_dict()["JWT"]
        response = requests.get(url="https://ksu24.kspu.edu/api/v2/my/profile/", cookies={'JWT': auth_cookie})
        data = response.json()
    else:
        return "<center><h1>Помилка!</h1> <br><h3>Напевно ви неправильно ввели логін або пароль!</h3></center>"

    return format_information(data)


@app.route('/', methods=["GET"])
def login():
    return login_page


if __name__ == '__main__':
    app.run()
    
