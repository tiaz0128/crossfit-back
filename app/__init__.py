from flask import Flask
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from flask_restx import Api

from app.config import DevConfig


db = SQLAlchemy()
migrate = Migrate()
api = Api(doc="/docs")


def create_app():
    app = Flask(__name__)

    CORS(app)
    app.config.from_object(DevConfig)

    # ORM
    db.init_app(app)
    migrate.init_app(app, db)
    from . import models

    # DOC
    api.init_app(app)
    from .views.members import ns

    api.add_namespace(ns, "/members")

    return app
