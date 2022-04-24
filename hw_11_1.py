# Домашняя работа - 11. Выводит данные из файла candidates.json через utils.py на веб-страницу.
from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def page_index():
    title = 'Енот Тёма'
    return render_template('index.html', title=title)


app.run(host='127.0.0.2')
