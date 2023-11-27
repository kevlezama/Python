from flask import Flask
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

from db import Base
from config import DevelopmentConfig

# Routes
from routes.index import index


db = SQLAlchemy(model_class=Base)

def create_app():

    #Application configuration
    app = Flask(__name__)
    app.config.from_object('config.DevelopmentConfig')

    #DB Init and migration
    db.init_app(app)
    migrate = Migrate(app, db)

    # Aplication blueprints
    app.register_blueprint(index)

    # Application Models
    from models.user import User

    #with app.app_context():
        #db.create_all()

    return app