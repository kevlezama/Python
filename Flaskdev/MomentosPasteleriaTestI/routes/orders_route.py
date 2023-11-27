
# Flask framework
from flask import Blueprint, jsonify, request

# Sqlalchemy ORM API
from sqlalchemy import select

# Application packages
from app import db
from models.client import Client

# Python buildin 
import uuid
import datetime


order_route  = Blueprint('orders' ,__name__)


@order_route.route('/orders/getall/activeorders', methods=['GET'])
def get_all_active_client():
    pass