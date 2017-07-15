#!venv/bin/python
import imp

from migrate.versioning import api

from config import SQLALCHEMY_DATABASE_URI, SQLALCHEMY_MIGRATE_REPO
from flaskbook import db

version = api.db_version(SQLALCHEMY_DATABASE_URI, SQLALCHEMY_MIGRATE_REPO)
migration = '%s/versions/%03d_migration.py' % (SQLALCHEMY_MIGRATE_REPO, (version + 1))

tmp_module = imp.new_module('old_model')
old_model = api.create_model(SQLALCHEMY_DATABASE_URI, SQLALCHEMY_MIGRATE_REPO)
exec(old_model, tmp_module.__dict__)

script = api.make_update_script_for_model(
    SQLALCHEMY_DATABASE_URI, SQLALCHEMY_MIGRATE_REPO,
    tmp_module.meta, db.metadata)
with open(migration, 'wt') as file:
    file.write(script)

api.upgrade(SQLALCHEMY_DATABASE_URI, SQLALCHEMY_MIGRATE_REPO)

version = api.db_version(SQLALCHEMY_DATABASE_URI, SQLALCHEMY_MIGRATE_REPO)
print('New migration saved: %s' % migration)
print('Current database version: %i' % version)
