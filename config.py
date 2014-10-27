import os


class Config(object):
    DEBUG = False
    TESTING = False
    CSRF_ENABLED = True
    SECRET_KEY = 'development key'
    USERNAME = 'admin'
    PASSWORD = 'default'
    SQLALCHEMY_DATABASE_URI = os.environ['DATABASE_URL']


class ProductionConfig(Config):
    ENVIRONMENT = 'production'
    DEBUG = False


class StagingConfig(Config):
    ENVIRONMENT = 'staging'
    DEVELOPMENT = True
    DEBUG = True


class DevelopmentConfig(Config):
    ENVIRONMENT = 'development'
    DEVELOPMENT = True
    DEBUG = True


class TestingConfig(Config):
    ENVIRONMENT = 'test'
    TESTING = True