import os
from flask import Flask
from flask.ext.openid import OpenID
from flask.ext.sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config.from_object(os.environ['APP_SETTINGS'])

db = SQLAlchemy(app)

oid = OpenID(app)

import todo.views
import authentication.views
