
# Flask framework
from flask import Blueprint, jsonify, request

# Sqlalchemy ORM API
from sqlalchemy import select

# Application packages
from config.dbconfig import db
from models.user import User

# Python buildin 
import uuid
import datetime

users_route  = Blueprint('users' ,__name__)

@users_route.route('/users/getall', methods=['GET','POST'])
def show_all_users() -> any:
    stm = select(User).order_by(User.user_id)
    user_query = db.session.execute(stm).all()
    return jsonify(user_query)


@users_route.route('/users/getall/user_by_id/<uuid:user_id>', methods=['GET'])
def get_user_by_id(user_id) -> any:

    stm = select(User).where(User.user_uid == user_id)
    users_by_id_result = db.session.execute(stm).scalar()

    return jsonify(users_by_id_result)

@users_route.route('/users/create', methods=['POST'])
def create_user() -> any:
    
    request_data = request.get_json()
    
    req_user_id = request_data['user_id']
    req_user_name =  request_data['user_name']
    req_user_last_name = request_data['user_last_name']
    req_user_tier = request_data['user_tier_rank']
    req_user_paid = request_data['user_paid']
    req_user_free = request_data['user_free']

    user_uuid = uuid.uuid4()
    user_created_data_timestamp = datetime.datetime.now()

    user = User(
        user_uuid,
        req_user_id,
        req_user_name, 
        req_user_last_name, 
        req_user_tier, 
        req_user_paid,
        req_user_free,
        user_created_data_timestamp
        )
    
    db.session.add(user)
    db.session.commit()
    db.session.close()

    return jsonify({"response":201})


    