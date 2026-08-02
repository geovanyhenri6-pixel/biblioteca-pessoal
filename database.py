import sqlite3
import os 
from flask import g
from config import Config

def get_db():

    if not hasattr(g, "db"):
        os.makedirs(os.path.dirname(Config.DATABASE ), exist_ok=True)
        g.db = sqlite3.connect(Config.DATABASE)
        g.db.row_factory = sqlite3.Row
        g.db.execute("PRAGMA foreign_keys = ON")

    return g.db

def close_db(e=None):
    db = g.pop("db", None) 

    if db is not None:
        db.close()

def init_db():
    db = get_db()
    with open("schema.sql", "r") as f:
        sql = f.read()

    db.executescript(sql)
    db.commit()