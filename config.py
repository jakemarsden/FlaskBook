import os

DIR_BASE = os.path.abspath(os.path.dirname(__file__))
DIR_STORAGE = os.path.join(DIR_BASE, 'storage')

DEBUG = True
TESTING = False
SERVER_HOST = '0.0.0.0'
SERVER_PORT = 5000

SQLALCHEMY_DATABASE_URI = 'sqlite:///%s/%s' % (DIR_STORAGE, 'app.db')
SQLALCHEMY_MIGRATE_REPO = os.path.join(DIR_STORAGE, 'db_repository')
SQLALCHEMY_TRACK_MODIFICATIONS = False

if not os.path.exists(DIR_STORAGE):
    os.makedirs(DIR_STORAGE)
