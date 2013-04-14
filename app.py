#! coding: utf-8

import sqlite3 as sq
import sys
from models.manager import Manager
from models.todo import  Todo

# set up manager.
manager = Manager()
manager.connect()
cur = manager.cur

todo = Todo(cur)

print todo.show_version()








