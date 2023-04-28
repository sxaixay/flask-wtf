from flask import Flask, render_template, redirect
from loginform import *

app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'


@app.route('/login', methods=['GET', 'POST'])
def login():
    LogForm = LoginForm()
    if LogForm.validate_on_submit():
        return redirect('/login')
    return render_template('color.html', title='Аварийный доступ', form=LogForm)


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
