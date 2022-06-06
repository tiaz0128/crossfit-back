from decouple import config

DB_ENGINE = config("DB_ENGINE")
DB_USERNAME = config("DB_USERNAME")
DB_PASS = config("DB_PASS")
DB_HOST = config("DB_HOST")
DB_PORT = config("DB_PORT")
DB_NAME = config("DB_NAME")

SQLALCHEMY_DATABASE_URI = (
    f"{DB_ENGINE}://{DB_USERNAME}:{DB_PASS}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
)
SQLALCHEMY_TRACK_MODIFICATIONS = False

SECRET_KEY = "crossfit_app"
