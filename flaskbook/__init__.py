from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy_imageattach.stores.fs import HttpExposedFileSystemStore

import config

app = Flask(__name__)
app.config.from_object('config')

db = SQLAlchemy(app)

image_store = HttpExposedFileSystemStore(path=config.IMAGE_STORE_PATH, prefix=config.IMAGE_STORE_PREFIX)
app.wsgi_app = image_store.wsgi_middleware(app.wsgi_app)

# noinspection PyUnresolvedReferences
from flaskbook.orm import models
# noinspection PyUnresolvedReferences
from flaskbook.ui import views
