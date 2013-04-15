#coding: utf-8
import datetime

class Todo(object):
    # bind to sqlite3's cursor.
    def __init__(self,cur,con):
        self.cur = cur
        self.con = con

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


    def insert(self,task_name):
        self.cur.execute("insert into todos(task) values('%s');" % task_name)

    def show_todos(self):
      d =   self.cur.execute("select * from todos").fetchall()
      return d

    def update(self,_id,task):
        stmt = """
        update todos
            set task = ?
            where id = ?;
        """
        self.cur.execute(stmt,(task,_id))
        self.con.commit()


    def where(self,_k):
        k =  _k.keys()[0]
        v = _k.values()[0]
        statement = """
        select * from todos where %s = :%s; """ % (k,k)

        res = self.cur.execute(statement,{k:v})
        return res
