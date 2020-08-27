import sqlite3


class ListTable:

    def __init__(self, table_name, *args):
        self.conn = sqlite3.connect("hadobit_db.db", check_same_thread=False)
        self.c = self.conn.cursor()
        self.table_name = table_name
        self.columns = ''
        if len(args) == 0:
            self.get_column_names()
        else:
            for i in args:
                self.columns += i
                self.columns += ', '
        self.add_type_to_columns()

    def create_table(self):
        self.c.execute("""
                CREATE TABLE IF NOT EXISTS {}({})
                """.format(self.table_name, self.columns_with_type))

    def append_to_table(self, values):
        self.vals = []
        for i in values:
            self.vals.append("'" + i + "',")
        self.vals = ' '.join(self.vals)
        # print("""INSERT INTO {}({}) VALUES({})""".format(
        #     self.table_name, self.columns[:-2], self.vals[:-1]))
        self.c.execute("""
            INSERT INTO {}({}) VALUES({})
        """.format(self.table_name, self.columns, self.vals[:-1]))

    # Adds an INT primary key and BLOB type to the rest of the columnns.
    def add_type_to_columns(self):
        self.column_list = self.columns.split(', ')
        self.column_list = self.column_list[:-1]
        # print(self.column_list)
        self.columns_with_type = []
        for i in self.column_list:
            self.columns_with_type.append(i + " BLOB")
        self.columns_with_type = 'id INTEGER PRIMARY KEY, ' + ', '.join(
            self.columns_with_type)
        return self.columns_with_type

    def read_all_rows(self):
        self.c.execute("SELECT * FROM {}".format(self.table_name))
        # print(c.description)
        return self.c.fetchall()

    def get_column_names(self):
        # c.execute("SELECT * FROM {}".format(self.table_name))
        self.c.execute("PRAGMA table_info({})".format(self.table_name))
        # print(c.fetchall())
        for i in self.c.fetchall():
            # print(i[1])
            if i[1] == "id":
                pass
            else:
                self.columns += i[1] + ', '
        self.columns = self.columns[:-2]
        # print(self.columns)
        # description = c.description
        # for i in description
        #     self.columns += i[0] + ", "
        # print(self.columns)
        return self.columns

    def read_column_names(self):
        self.c.execute("PRAGMA table_info({})".format(self.table_name))
        for i in self.c.fetchall():
            print(i)

    def add_column_to_table(self, column, column_type):
        self.c.execute("ALTER TABLE {} ADD COLUMN {} {}".format(self.table_name, column, column_type),
                       )
