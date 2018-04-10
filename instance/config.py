config = {
    'SECRET': 'secret_word',
    'APP_STAGE': 'dev',
    'DATABASE_URL': 'postgresql://postgres:logan1996n@localhost/flask_api',
    'DATABASE_URL_TESTING': 'postgresql://postgres:logan1996n@localhost/test_db'
}

class Config(object):
    """ Parent configuration class """
    DEBUG = False
    CSRF_ENABLED = True
    SECRET = config.get('SECRET')
    SQLALCHEMY_DATABASE_URI = config.get('DATABASE_URL')

class TestingConfig(Config):
    """ Testing environment configuration """
    """  - with a separate test database """
    TESTING = True
    SQLALCHEMY_DATABASE_URI = config.get('DATABASE_URL_TESTING')
    DEBUG = True

class DevConfig(Config):
    """ Dev stage configuration """
    DEBUG = True

class QAConfig(Config):
    """ QA stage configuration """
    DEBUG = True

class ProdConfig(Config):
    """ Prod stage configuration """
    DEBUG = False
    TESTING = False

app_config = {
    'testing': TestingConfig,
    'dev': DevConfig,
    'qa': QAConfig,
    'prod': ProdConfig,
}