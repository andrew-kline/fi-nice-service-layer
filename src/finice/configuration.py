from finice.settings import PG_USER, PG_PASS


class Config(object):
    """
    Configuration base, for all environments.
    """

    DEBUG = False
    TESTING = False
    DATABASE_URI = f"postgresql://{PG_USER}:{PG_PASS}@localhost/finice"


class ProductionConfig(Config):
    """
    Production environment specific configurations.
    """


class DevelopmentConfig(Config):
    DEBUG = True


class TestingConfig(Config):
    DEBUG = True
    TESTING = True
    DATABASE_URI = "sqlite:///test_database.db"


class LocalConfig(Config):
    DEBUG = True
    DATABASE_URI = "sqlite:///database.db"
