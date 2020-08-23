class ListTable:

    def __init__(self, conn, table_name, *args):
        self.conn = conn
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
        c = self.conn.cursor()
        c.execute("""
                CREATE TABLE IF NOT EXISTS {}({})
                """.format(self.table_name, self.columns_with_type))

    def append_to_table(self, values):
        c = self.conn.cursor()
        self.vals = []
        for i in values:
            self.vals.append("'" + i + "',")
        self.vals = ' '.join(self.vals)
        # print("""INSERT INTO {}({}) VALUES({})""".format(
        #     self.table_name, self.columns[:-2], self.vals[:-1]))
        c.execute("""
            INSERT INTO {}({}) VALUES({})
        """.format(self.table_name, self.columns, self.vals[:-1]))

    def add_type_to_columns(self):
        self.column_list = self.columns.split(', ')
        self.column_list = self.column_list[:-1]
        # print(self.column_list)
        self.columns_with_type = []
        for i in self.column_list:
            self.columns_with_type.append(i + " BLOB")
            # try:
            #     float(i)
            #     self.columns_with_type.append(i + " INTEGER")
            # except ValueError:
            #     self.columns_with_type.append(i + " TEXT")
        self.columns_with_type = 'id INTEGER PRIMARY KEY, ' + ', '.join(
            self.columns_with_type)
        return self.columns_with_type

    def read_all_rows(self):
        c = self.conn.cursor()
        c.execute("SELECT * FROM {}".format(self.table_name))
        # print(c.description)
        return c.fetchall()

    def get_column_names(self):
        c = self.conn.cursor()
        # c.execute("SELECT * FROM {}".format(self.table_name))
        c.execute("PRAGMA table_info({})".format(self.table_name))
        # print(c.fetchall())
        for i in c.fetchall():
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

    def add_column_to_table(self, column, column_type):
        c = self.conn.cursor()
        c.execute("ALTER TABLE {} ADD COLUMN {} {}".format(self.table_name, column, column_type),
                  )
