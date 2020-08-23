import sqlite3
from ListTable import ListTable
from datetime import date, timedelta


def create_connection(db_name):
    conn = sqlite3.connect(db_name)
    return conn


if __name__ == "__main__":
    conn = create_connection("hadobit_db.db")
    todolist = ListTable(conn, "ToDoList")  # date, task, todolist, completed
    # print(date.today())
    with conn:
        # todolist.add_column_to_table("completed", "TEXT")
        # todolist.read_all_rows()
        # c = conn.cursor()
        # c.execute("SELECT * FROM ToDoList")
        # print(c.fetchall())
        # todolist.append_to_table(
        #     [str(date.today()), 'test this out', 'asdf', 'True'])
        # print(columns)
        print(todolist.read_all_rows())
        conn.commit()
