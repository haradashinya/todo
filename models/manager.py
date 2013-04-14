import sqlite3 as lite
class Manager():
    def __init__(self):
        print "init"
        pass

    def connect(self):
        self.con = lite.connect("todo.db")
        with self.con:
            cur = self.con.cursor()
            cur.execute("select sqlite_version()")
            data = cur.fetchone()
            co = cur.fetchone()
            self.cur = cur
            print "setup"






