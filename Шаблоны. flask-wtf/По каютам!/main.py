from flask import Flask, render_template

app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'


@app.route('/cabins', methods=['GET', 'POST'])
def info():
    return render_template('color.html', user_list=users)


if __name__ == '__main__':
    users = ["Ридли Скотт", "Энди Уир", "Марк Уотни", "Венката Капур", "Тедди Сандерс", "Шон Бин"]
    app.run(port=8080, host='127.0.0.1')
