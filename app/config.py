from decouple import config


class Config:
    SECRET_KEY = config("SECRET_KEY")
    SQLALCHEMY_TRACK_MODIFICATIONS = config("SQLALCHEMY_TRACK_MODIFICATIONS", cast=bool)


class DevConfig(Config):
    DEBUG = True
    SQLALCHEMY_ECHO = True

    FLASK_ENV = config("FLASK_ENV")

    DB_ENGINE = config("DB_ENGINE")
    DB_USERNAME = config("DB_USERNAME")
    DB_PASS = config("DB_PASS")
    DB_HOST = config("DB_HOST")
    DB_PORT = config("DB_PORT")
    DB_NAME = config("DB_NAME")

    SQLALCHEMY_DATABASE_URI = (
        f"{DB_ENGINE}://{DB_USERNAME}:{DB_PASS}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
    )


class ProdConfig(Config):
    pass


class TestConfig(Config):
    pass
