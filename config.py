import os

basedir = os.path.abspath(os.path.dirname(__file__))


class BaseConfig(object):
    SQLALCHEMY_TRACK_MODIFICATIONS = True


class DevelopConfig(BaseConfig):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
                              'sqlite:///' + os.path.join(basedir, 'app.db')


class ProductConfig(BaseConfig):
    DEBUG = False
