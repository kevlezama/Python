# Flask framework
from flask import Blueprint, jsonify, request

# Sqlalchemy ORM API
from sqlalchemy import select

# Application packages
from dbconfig import db
from models.items import Items

# Python buildin 
import uuid
import datetime


item_route  = Blueprint('items' ,__name__)


ITEMS_ORDER_BY_ITEM_PRICE_STM = select(Items).order_by(Items.item_price)
AVAILABLE_ITEMS_ORDER_BY_ITEM_PRICE = select(Items).where(Items.item_availability == "true")


@item_route.route("/items/allitems", methods=['GET'])
def get_all_items():
    query_execution = db.session.execute(ITEMS_ORDER_BY_ITEM_PRICE_STM).all()
    print(query_execution)
    return jsonify(query_execution)


@item_route.route("/items/availitems", methods=['GET'])
def get_available_items():
    query_execution = db.session.execute(AVAILABLE_ITEMS_ORDER_BY_ITEM_PRICE).all()
    print(query_execution)
    return jsonify(query_execution)


@item_route.route("/items/allitems", methods=['GET'])
def create_items():

    request_data = request.get_data()
    
    print(request_data)


    
