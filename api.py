from ListTable import ListTable
import sqlite3
from datetime import date, timedelta
import flask
from flask import jsonify

app = flask.Flask(__name__)
app.config["DEBUG"]


@app.route("/", methods=["GET"])
def home():
    return jsonify(list_to_json)


def create_connection(db_name):
    conn = sqlite3.connect(db_name)
    return conn


conn = create_connection("hadobit_db.db")
todolist = ListTable(conn, "ToDoList")
with conn:
    conn.row_factory = sqlite3.Row
    list_to_json = []
    for row in todolist.read_all_rows():
        list_to_json.append(dict(row))
        # print(dict(row))

# print(jsonify(list_to_json))
app.run()
