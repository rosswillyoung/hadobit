from ToDoList import ToDoList
import sqlite3
from datetime import date, timedelta
import flask
from flask import jsonify

app = flask.Flask(__name__)
app.config["DEBUG"]


# conn = sqlite3.connect("hadobit_db.db")
# conn.row_factory = sqlite3.Row
todolist = ToDoList()

# c = conn.cursor()


@app.route("/todo", methods=["GET"])
def home():
    list_to_json = []
    for row in todolist.read_all_rows():
        list_to_json.append(dict(row))
        # print(dict(row))
    return jsonify(list_to_json)


# print(jsonify(list_to_json))
app.run()
