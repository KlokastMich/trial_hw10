from flask import Flask
from funcs import *

candidates = load_file()

app = Flask(__name__)


@app.route("/")
def print_candidates():
    string = ""
    for person in candidates.values():
        string += f'''Имя кандидата - {person["name"]}<br>
                      Позиция: {person["position"]}<br>
                      Навыки: {person["skills"]}<br><br>'''
    return string


@app.route("/candidate/<int:id>")
def print_pictures(id):
    string = ""
    for person in candidates.values():
        if id == person["id"]:
            string += f'''<img src="{person['picture']}"><br><br>
                          Имя кандидата - {person["name"]}<br>
                          Позиция: {person["position"]}<br>
                          Навыки: {person["skills"]}<br><br>'''
    return string


@app.route("/skill/<search>")
def skill_search(search):
    string = ""
    for person in candidates.values():
        skill = person["skills"].lower().split(", ")
        if search in skill:
            string += f'''<img src="{person['picture']}"><br><br>
                          Имя кандидата - {person["name"]}<br>
                          Позиция: {person["position"]}<br>
                          Навыки: {person["skills"]}<br><br>'''
    return string


app.run()
