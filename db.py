import sqlite3
from flask import current_app, g

DATABASE = "./instance/german.db"

def get_db():
    try:
        db = getattr(g, '_database', None)
        if db is None:
            db = g._database = sqlite3.connect(DATABASE)
        return db
    except sqlite3.Error as e:
        print(f"Database connection error: {e}")

def close_db(e=None):
    """ termination"""
    db = g.pop('db', None)

    if db is not None:
        db.close()
