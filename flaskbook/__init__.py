from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config.from_object('config')

db = SQLAlchemy(app)

# noinspection PyUnresolvedReferences
from flaskbook.orm import models
# noinspection PyUnresolvedReferences
from flaskbook.ui import views
