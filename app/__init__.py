from datetime import datetime
from flask import Flask
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS

# from flask_wtf.csrf import CSRFProtect

import config

db = SQLAlchemy()
migrate = Migrate()
# csrf = CSRFProtect()


def create_app():
    app = Flask(__name__)
    CORS(app)
    # csrf.init_app(app)
    app.config.from_object(config)

    # ORM
    db.init_app(app)
    migrate.init_app(app, db)
    from . import models

    # blueprint
    from .views import index, box, members, member

    app.register_blueprint(index.bp)
    app.register_blueprint(box.bp)
    app.register_blueprint(members.bp)
    app.register_blueprint(member.bp)

    return app
