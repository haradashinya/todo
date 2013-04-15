#! coding: utf-8

import sqlite3 as sq
import sys
from models.manager import Manager
from models.todo import  Todo

# set up manager.
manager = Manager()

# bind cur,con to manager
todo = Todo(manager)
todo.drop_table()
todo.create_table()
todo.find(2).remove()
todo.find(1).update("wash the car")
todo.create({"task": "bar"})
todo.create({"task": "hoge"})

print todo.show_todos()







