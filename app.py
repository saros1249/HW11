# Домашняя работа - 11. Выводит данные из файла candidates.json через utils.py на веб-страницу.
from flask import Flask, render_template
from utils import load_candidates_from_json, get_candidates_by_name, get_candidate, get_candidates_by_skill

app = Flask(__name__)


@app.route("/")
def page_index():
    return render_template('list.html', candidates=load_candidates_from_json())


@app.route("/candidates/<int:candidate_id>")
def page_candidates(candidate_id):
    return render_template('card.html', candidates=get_candidate(candidate_id))


@app.route("/search/<candidate_name>")
def page_candidate_name(candidate_name):
    return render_template('search.html', candidates=load_candidates_from_json(),
                           candidate_name=get_candidates_by_name(candidate_name),
                           count=len(get_candidates_by_name(candidate_name)))


@app.route("/skills/<skill>")
def page_skills(skill):
    return render_template('skill.html', candidates=load_candidates_from_json(),
                           candidate_skill_name=get_candidates_by_skill(skill))


app.run()
