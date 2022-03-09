from flask_sqlalchemy import SQLAlchemy
from flask_bootstrap import Bootstrap
from flask import Flask
from config import config_options
from flask_login import LoginManager
from flask_mail import Mail
from flask_simplemde import SimpleMDE


login_manager = LoginManager()
login_manager.session_protection = 'strong'
login_manager.login_view = 'auth.login'

bootstrap = Bootstrap()
db = SQLAlchemy()
mail = Mail()
simple = SimpleMDE()

def create_app(config_name):
    # Initializing application
    app = Flask(__name__,template_folder='templates', static_folder='static')

    # Creating the app configurations
    app.config.from_object(config_options[config_name])

    # Initializing flask extensions
    bootstrap.init_app(app)

    # Initalizing database
    db.init_app(app)

    # Initializing login manager
    login_manager.init_app(app)

    # Initializing mail
    mail.init_app(app)

    #initializing simple review editor
    simple.init_app(app)

    # Registering the blueprint
    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    from .auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint, url_prefix = '/authenticate')

    # setting config
    # from .requests import configure_request
    # configure_request(app)

    return app