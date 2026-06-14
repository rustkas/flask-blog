"""A simple Flask application that returns "Hello World!" when accessed at the root URL."""
import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from flask_mail import Mail

db = SQLAlchemy()
bcrypt = Bcrypt()
login_manager = LoginManager()
mail = Mail()

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
    
    app.config['MAIL_SERVER'] = 'smtp.googlemail.com'
    app.config['MAIL_PORT'] = 587
    app.config['MAIL_USE_TLS'] = True
    app.config['MAIL_USERNAME'] = os.environ.get('EMAIL_USER')
    app.config['MAIL_PASSWORD'] = os.environ.get('EMAIL_PASS')
    mail.init_app(app)

    from . import routes
    app.register_blueprint(routes.bp)
    return app
