__author__ = 'tygern'

import sqlite3
from flask import Flask, g
from contextlib import closing
import os

app = Flask(__name__)
app.config.from_object(os.environ['APP_SETTINGS'])

print '*' * 80
print 'Starting Mercury in', app.config['ENVIRONMENT']
print '*' * 80

import todo.views
import security.views

def connect_db():
    return sqlite3.connect(app.config['DATABASE'])

def init_db():
    with closing(connect_db()) as db:
        with app.open_resource('schema.sql', mode='r') as f:
            db.cursor().executescript(f.read())
        db.commit()

@app.before_request
def before_request():
    g.db = connect_db()

@app.teardown_request
def teardown_request(exception):
    db = getattr(g, 'db', None)
    if db is not None:
        db.close()
