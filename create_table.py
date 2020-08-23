import sqlite3
from sqlite3 import Error


def create_connection(db_file):
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        return conn
    except Error as e:
        print(e)
    return conn


def create_table(conn, table_name, column_list):
    try:
        c = conn.cursor()
        # THIS IS THE PROPER WAY TO ADD VARIABLE # OF COLUMNS
        c.execute("""
                    CREATE TABLE IF NOT EXISTS {}(
                        {}
                    )
        """.format(table_name, *column_list))
    except Error as e:
        print(e)


def add_row_to_table(conn, table_name, column_list, row_data):
    try:
        c = conn.cursor()
        c.execute("""
                INSERT INTO {}({}) VALUES({})
        """.format(table_name, *column_list, *row_data))
    except Error as e:
        print(e)


def main():

    conn = create_connection("hadobit_db.db")

    if conn is not None:
        # create_table(conn, 'testing2', ['wow', 'dope', 'cool'])
        c = conn.cursor()
        c.execute("INSERT INTO testing2(wow, dope, cool) VALUES(?,?,?)",
                  ("wowza", "bazinga", "lakjadhf;sdjfh"))
        conn.commit()
        conn.close()


if __name__ == "__main__":
    main()
