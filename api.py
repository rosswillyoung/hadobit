from ToDoList import ToDoList
from ListTable import ListTable
import sqlite3
from datetime import date, timedelta
import flask
from flask import jsonify, request, redirect, url_for
from flask_cors import CORS

app = flask.Flask(__name__)
app.config["DEBUG"]
CORS(app)


# conn = sqlite3.connect("hadobit_db.db")
# conn.row_factory = sqlite3.Row
todolist = ToDoList()

# c = conn.cursor()


@app.route("/todo", methods=["GET", "POST"])
def home():
    try:
        if request.method == "POST":
            # todolist.append_row(str(date.today()), "test",
            #                     "test post request", "False")
            data = request.get_json()
            todolist.add_task_today(data['task'])
            # print(data['task'])
            return "< h1 > row appended < /h1 >"
        else:
            list_to_json = []
            for row in todolist.read_todays_tasks():
                list_to_json.append(dict(row))
                # print(dict(row))
            return jsonify(list_to_json)
    except Exception as e:
        print(e)


@app.route("/complete", methods=["POST"])
def query():
    # args = request.args
    # print(args)
    data = request.get_json()
    # print(data['id'])
    todolist.change_row_to_complete(data['id'])
    # return "No query received", 200
    return "Row Completed"


@app.route("/createlist", methods=["POST"])
def create_list():
    data = request.get_json()
    print(data["tracker"])
    print(data["tracker_items"])
    new_tracker = ListTable(data["tracker"], data["tracker_items"])
    new_tracker.create_table()
    return "None"


@app.route("/addsubtask", methods=["POST"])
def add_subtask():
    data = request.get_json()
    # print(data["id"])
    print(data["subtask"])
    todolist.append_to_subtask(data["subtask"], data["id"])
    return "None"


# print(jsonify(list_to_json))
app.run()
