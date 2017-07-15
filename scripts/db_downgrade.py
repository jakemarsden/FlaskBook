#!venv/bin/python
from migrate.versioning import api

from config import SQLALCHEMY_DATABASE_URI, SQLALCHEMY_MIGRATE_REPO

version = api.db_version(SQLALCHEMY_DATABASE_URI, SQLALCHEMY_MIGRATE_REPO)
api.downgrade(SQLALCHEMY_DATABASE_URI, SQLALCHEMY_MIGRATE_REPO, (version - 1))

version = api.db_version(SQLALCHEMY_DATABASE_URI, SQLALCHEMY_MIGRATE_REPO)
print('Current database version: %i' % version)
