from flask import Flask
from flask_sqlalchemy import SQLAlchemy

import config

app = Flask(__name__)
app.config.from_object('config')
app.wsgi_app = config.SQLALCHEMY_IMAGE_STORE.wsgi_middleware(app.wsgi_app)

db = SQLAlchemy(app)

# noinspection PyUnresolvedReferences
from flaskbook.orm import models
# noinspection PyUnresolvedReferences
from flaskbook.ui import views
