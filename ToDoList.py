import sqlite3
# from ListTable import ListTable
from datetime import date, timedelta


class ToDoList():
    def __init__(self):
        self.conn = sqlite3.connect("hadobit_db.db", check_same_thread=False)
        self.conn.row_factory = sqlite3.Row
        self.c = self.conn.cursor()
        self.table_name = "ToDoList"
        self.columns = "id, date, task, subtask, completed"
        self.columns_with_type = "id INTEGER PRIMARY KEY, date BLOB, task BLOB, subtasks BLOB, completed TEXT"

    def read_all_rows(self):
        with self.conn:
            self.c.execute("SELECT * FROM {}".format(self.table_name))
            return self.c.fetchall()

    def read_todays_tasks(self):
        # print('Reading todays tasks')
        with self.conn:
            self.c.execute(
                "SELECT * FROM ToDoList WHERE date = ?", (str(date.today()),))
            return self.c.fetchall()

    def append_row(self, *vals):
        self.vals = []
        for i in vals:
            self.vals.append("'" + i + "',")
        self.vals = ' '.join(self.vals)
        self.c.execute("""
                INSERT INTO ToDoList(date, task, subtasks, completed) VALUES({})
                """.format(self.vals[:-1]))
        self.conn.commit()

    def add_task_today(self, task):
        # self.task = "'" + str(task) + "'"
        today = str(date.today())
        # self.c.execute("INSERT INTO ToDoList(date, task, subtasks, completed) VALUES(? {} ? ?)".format(
        #     self.task), (str(date.today()), "'None'", "'False'"))
        self.c.execute(
            f"INSERT INTO ToDoList(date, task, completed) VALUES('{today}', '{task}', 'False')")
        # .format("'" + str(date.today()) + "', " + self.task + ", ''" + ", 'False'"))
        self.conn.commit()

    def change_row_to_complete(self, row_id):
        self.c.execute("""
                        UPDATE ToDoList SET completed = 'True'
                        WHERE id = {}
                    """.format(row_id))
        self.conn.commit()
        pass

    def add_subtask(self, subtask, row_id):
        self.subtask = "'" + subtask + "'"
        # self.c.execute("""
        #                 UPDATE ToDoList SET subtasks = {} WHERE id = {}
        #                 """.format(self.subtask, row_id))
        self.c.execute(
            f"""UPDATE ToDoList SET subtasks = {self.subtask} WHERE id = {row_id}""")
        self.conn.commit()
        print("added subtask")
        pass

    def append_to_subtask(self, subtask, row_id):
        self.c.execute("""
                        SELECT subtasks FROM ToDoList WHERE id = {} 
                    """.format(row_id))
        # self.subtasks = self.c.fetchone()
        try:
            self.subtasks = ", ".join(self.c.fetchall()[0])
            self.subtasks = "'" + self.subtasks + ", " + subtask + "'"
            self.c.execute("""
                        UPDATE ToDoList SET subtasks = {} WHERE id = {}
                        """.format(self.subtasks, row_id))
        except TypeError:
            self.c.execute(
                f"UPDATE ToDoList SET subtasks = '{subtask}' WHERE id ={row_id}")
        # return self.subtasks
        # pass

    def remove_task(self, row_id):
        with self.conn:
            self.c.execute("DELETE FROM ToDoList WHERE id=?", (row_id,))
        pass
