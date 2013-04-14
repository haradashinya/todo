#coding: utf-8

class Todo(object):
    # bind to sqlite3's cursor.
    def __init__(self,cur):
        self.cur = cur

    def show_version(self):
        return self.cur.execute("select sqlite_version()").fetchone()

    def create_table(self):
        self.cur.execute("""
        create table if not exists todos(
            id integer primary key,
            task Text,
            updated datetime);
            """
            )

    def drop_table(self):
        self.cur.execute("""
        drop table if exists todos
        """)


    def insert(self,task_name):
        self.cur.execute("insert into todos(task) values('%s');" % task_name)

    def show_todos(self):
      d =   self.cur.execute("select * from todos").fetchall()
      print d

    def where(self,_k):
        v = "hello"

        statement = """
        select * from todos where task = :task; """

        self.cur.execute(statement,{"task":"hello"})

        return self





