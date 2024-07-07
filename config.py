import os

basedir = os.path.abspath(os.path.dirname(__file__))


class Config:
    DEBUG = True
    SQLALCHEMY_ECHO = True
    # SECRET_KEY = os.environ.get('SECRET_KEY', 'SmFjb2IgS2FwbGFuLU1vc3MgaXMgYSBoZXJv')
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URI')\
        or 'sqlite:///' + os.path.join(basedir, 'nonscheduled_flights_register.sqlite3') # .db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False