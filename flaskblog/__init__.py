"""A simple Flask application that returns "Hello World!" when accessed at the root URL."""

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager

db = SQLAlchemy()
bcrypt = Bcrypt()
login_manager = LoginManager()


def create_app():
    """Create app"""
    app = Flask(__name__)
    app.config["SECRET_KEY"] = "ddb6bc214b788a8a7711ad104220d603"
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///site.db"
    db.init_app(app)

    bcrypt.init_app(app)
    login_manager.init_app(app)
    login_manager.login_view = 'blog.login' # type: ignore
    login_manager.login_message_category = 'info'
    from . import routes
    app.register_blueprint(routes.bp)
    return app
