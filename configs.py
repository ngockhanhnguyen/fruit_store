from builtins import object


class Config(object):
    """Base config, uses staging database server."""
    DEBUG = False
    TESTING = False
    HOST = "0.0.0.0"
    PORT = 8080
    LOGGER_CONFIG_PATH = "logger.conf"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_DATABASE_URI = 'sqlite:///:memory:'


class ProductionConfig(Config):
    """Uses production database server."""
    SQLALCHEMY_DATABASE_URI = "postgresql+psycopg2://fruitst:8sYdhrF59+EtvfHue+Q=@postgres:5432/fruitst"


class DevelopmentConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = "postgresql+psycopg2://fruitst:8sYdhrF59+EtvfHue+Q=@localhost:5432/fruitst"


class TestingConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'sqlite://test.db'
