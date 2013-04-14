#coding: utf-8

class Todo(object):
    # bind to sqlite3's cursor.
    def __init__(self,cur):
        self.cur = cur

    def show_version(self):
        return self.cur.execute("select sqlite_version()").fetchone()

    def create(self,task_name):
        pass

