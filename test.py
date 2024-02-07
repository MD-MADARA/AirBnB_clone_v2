#!/usr/bin/python3
""" Test .get() and .count() methods
"""
from models import storage
from models.state import State

res = storage.all()
for s in res:
    print("djdjjd")
    print(s.name)
