
# Flask framework
from flask import Blueprint, jsonify, request

# Sqlalchemy ORM API
from sqlalchemy import select

# Application packages
from config.dbconfig import db
from models.user import User

users_route  = Blueprint('users' ,__name__)

@users_route.route('/users/getall', methods=['GET','POST'])
def show_all_users() -> any:
    user_query = User.query.all()
    return jsonify(user_query)


@users_route.route('/users/getall/user_by_id/<uuid:user_id>', methods=['GET'])
def get_user_by_id(user_id) -> any:

    stm = select(User).where(User.user_uid == user_id)
    users_by_id_result = db.session.execute(stm).scalar()

    return jsonify(users_by_id_result)

@users_route.route('/users/create', method=['POST'])
def create_user() -> any:
    
    request_data = request.get_json()
    
    request_user_name =  request_data['user_']


    user = User()
    db.session.add(user)
    db.session.commit()


    