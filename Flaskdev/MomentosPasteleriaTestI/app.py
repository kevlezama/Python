from flask import Flask
from flask_migrate import Migrate

from dbconfig import db
from config import DevelopmentConfig

# Routes
from routes.index import index
from routes.user_route import users_route
from routes.client_route import client_route
from routes.orders_route import order_route
from routes.items_route import item_route

def create_app():

    #Application configuration
    app = Flask(__name__)
    app.config.from_object('config.DevelopmentConfig')

    #DB Init and migration
    db.init_app(app)
    migrate = Migrate(app, db)

    # Aplication blueprints
    app.register_blueprint(index)
    app.register_blueprint(users_route)
    app.register_blueprint(client_route)
    app.register_blueprint(order_route)
    app.register_blueprint(item_route)

    # Application Models
    from models.user2 import User
    from models.client import Client
    from models.client_address import Client_adress_model
    from models.items import Items
    from models.orders import Orders
    
    #with app.app_context():
        #db.drop_all()
        #db.create_all()

    return app