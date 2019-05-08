from flask import Flask, render_template
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from config import config

bootstrap = Bootstrap()
db = SQLAlchemy()

def create_app(config_name):
    application = Flask(__name__)
    application.config.from_object(config[config_name])
    config[config_name].init_app(application)

    bootstrap.init_app(application)    
    db.init_app(application)

    from .main import main as main_blueprint
    application.register_blueprint(main_blueprint)

    return application