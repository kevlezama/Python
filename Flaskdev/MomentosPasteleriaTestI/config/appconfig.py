from flask import Flask
from flask_migrate import Migrate

# Db Config

from config.dbconfig import db

# Routes

from .urlsconfig import index
from .urlsconfig import users_route

#from routes.user_route import users_route

def create_app():

    #Application configuration
    app = Flask(__name__)
    app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql+psycopg2://postgres:admin@localhost/MP"
    app.config["SQLALCHEMY_ECHO"] = True
    app.config["SQLALCHEMY_RECORD_QUERIES"] = True
    app.config["SQLALCHEMY_TRACK_MODIFICATION"] = False
    app.config['SECRET_KEY'] = 'DEV'
    db.init_app(app)

    migrate = Migrate(app, db)

    # Aplication blueprints

    app.register_blueprint(index)
    app.register_blueprint(users_route)

    # Application Models

    from models.user import User

    #with app.app_context():

        #db.create_all()

    return app