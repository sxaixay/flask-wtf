from flask import Flask, render_template, url_for
import random

app = Flask(__name__)


@app.route("/train/<prof>")
def training(prof):
    words = prof.split()
    urfor = url_for('static', filename="img/" + ( "sci.jpg" if "строитель" in words or "инженер" in words else "ing.jpg"))
    return render_template('training.html', title="Симулятор", source=urfor)


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')