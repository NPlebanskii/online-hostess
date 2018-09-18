config = {
    'SECRET': '}\xd3`C\xf8\xf8\x91F\xd1\xcc\xfc\xeea'
    '\x80\x8eU\x8c\xe6\xefp\xcf\x1b\xb7\xcc',
    'APP_STAGE': 'dev',
    'DATABASE_URL': 'postgresql://postgres:Logan1996n@localhost/test_db',
    'DATABASE_URL_TESTING': 'postgresql://postgres:Logan1996n@'
    'localhost/test_db'
}


class Config(object):
    """ Parent configuration class """
    DEBUG = False
    CSRF_ENABLED = True
    JWT_SECRET_KEY = config.get('SECRET')
    SQLALCHEMY_DATABASE_URI = config.get('DATABASE_URL')
    BCRYPT_LOG_ROUNDS = 13


class TestingConfig(Config):
    """ Testing environment configuration """
    """  - with a separate test database """
    TESTING = True
    SQLALCHEMY_DATABASE_URI = config.get('DATABASE_URL_TESTING')
    DEBUG = True
    BCRYPT_LOG_ROUNDS = 4


class DevConfig(Config):
    """ Dev stage configuration """
    DEBUG = True
    BCRYPT_LOG_ROUNDS = 4


class QAConfig(Config):
    """ QA stage configuration """
    DEBUG = True
    BCRYPT_LOG_ROUNDS = 4


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
