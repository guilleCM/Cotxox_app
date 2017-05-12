import os

DEBUG = True
SECRET_KEY = 'superdificil'

#DATABASE CONNECTION
basedir = os.path.abspath(os.path.dirname(__file__))
SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'db/cotxox.db')
SQLALCHEMY_MIGRATE_REPO = os.path.join(basedir, 'db_repository')