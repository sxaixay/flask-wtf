from flask import Flask, render_template, url_for

app = Flask(__name__)


@app.route('/auto_answer')
@app.route('/answer')
def auto_answer():
    return render_template('base.html', title=dictinaty["title"], dict_items=dictinaty,
                           url=url_for('static', filename='css/style.css'))


if __name__ == '__main__':
    dictinaty = {"title": "Анкета", "surname": "Watny", "name": "Mark",
                 "education": "выше среднего", "profession": "штурман марсохода",
                 "sex": "male", "motivation": "Всегда мечтал застрять на Марсе!",
                 "ready": True}
    app.run(port=8080, host='127.0.0.1')
