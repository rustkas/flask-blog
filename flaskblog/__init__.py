"""A simple Flask application that returns "Hello World!" when accessed at the root URL."""

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from . import routes

db = SQLAlchemy()


def create_app():
    """Create app"""
    app = Flask(__name__)
    app.config["SECRET_KEY"] = "ddb6bc214b788a8a7711ad104220d603"
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///site.db"
    db.init_app(app)

    app.register_blueprint(routes.bp)
    return app
