import sqlite3 as lite
class Manager():
    def __init__(self):
        print "init"
    def connect(self):
        con = lite.connect("todo.db")
        with con:
            cur = con.cursor()
            cur.execute("select sqlite_version()")
            data = cur.fetchone()
            co = cur.fetchone()
            self.cur = cur
            print "setup"






