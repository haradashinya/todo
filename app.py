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
todo.insert("hello")
todo.insert("nobinobiru")
todo.insert("foobar0219")
todo.delete(1)


todo.update(2,"o219")


print todo.show_todos()







