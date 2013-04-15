#coding: utf-8
import datetime

class Todo(object):
    # bind to sqlite3's cursor.
    def __init__(self,manager):
        self.stack = {}
        self.cur = manager.cur
        self.con = manager.con

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

    # delete todo from todos table.
    def delete(self,_id):
        stmt = """
        delete from todos where id = %i
        """ % _id
        self.cur.execute(stmt)

    def create(self,arg):
        keys = arg.keys()
        for i in keys:
            self.cur.execute("insert into todos(%s) values('%s');" % (i,arg[i]))

    def insert(self,task_name):
        self.cur.execute("insert into todos(task) values('%s');" % task_name)

    def show_todos(self):
      d =   self.cur.execute("select * from todos").fetchall()
      return d

    def find(self,_id):
        stmt = """
        select * from todos where id = %i
        """ % _id
        self.cur.execute(stmt)
        self.stack["id"] = _id
        return self


    def update(self,task):
        stmt = """
        update todos
            set task = ?
            where id = ?;
        """
        self.cur.execute(stmt,(task,self.stack["id"]))
        self.con.commit()
        self.stack = {}



    def remove(self):
        _id = self.stack["id"]
        stmt = """
        delete from todos where id = %i
        """ % _id
        self.cur.execute(stmt)
        # set init the stack.

