import os

basedir = os.path.abspath(os.path.dirname(__file__))


class Config:
    SECRET_KEY = "very-secret-dev-key"
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URI')\
        or 'sqlite:///' + os.path.join(basedir, 'db.sqlite')
    SQLALCHEMY_TRACK_MODIFICATIONS = False