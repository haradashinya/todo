#! coding: utf-8

import sqlite3 as sq
import sys
from models.manager import Manager
from models.todo import  Todo

# set up manager.
manager = Manager()
manager.connect()
cur = manager.cur
con = manager.con
todo = Todo(cur,con)
print todo.show_version()
todo.drop_table()
todo.create_table()
todo.insert("hello")
todo.insert("nobinobiru")
todo.show_todos()


print todo.where({"task":"nobinobiru"}).fetchone()

print todo.update(1,"hello")







