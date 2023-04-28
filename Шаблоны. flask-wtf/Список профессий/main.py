from flask import Flask, render_template

app = Flask(__name__)


@app.route('/index/<title>/<typ>')
def mission(title, typ):
    list_professions = ["Программист", "Врач", "Учитель", "экзобиолог", "пилот дронов", "инженер по терраформированию"]
    return render_template('base.html', title=title, typ=typ, list_prof=list_professions)


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
