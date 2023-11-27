
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


client_route  = Blueprint('clients' ,__name__)

@client_route.route('/clients/getall/clients', methods=['GET'])
def get_all_clients():
    stm = select(Client).order_by(Client.client_id)
    query_execution = db.session.execute(stm).all()
    return jsonify(query_execution, )

@client_route.route('/clients/getall/activeclients', methods=['GET'])
def get_all_active_client():
    pass

@client_route.route('/clients/createclient', methods=['POST'])
def create_new_client() -> any:

    request_data = request.get_json()

    clt_id = request_data['client_id']
    clt_name = request_data['client_name'] 
    clt_last_name = request_data['client_last_name']
    clt_email = request_data['client_email']
    clt_state =  request_data['client_state']
    clt_city = request_data['client_city']
    clt_delivery_addres = request_data['client_delivery_address']
    clt_orders = {}
    #user_uuid = uuid.uuid4()
    user_created_data_timestamp = datetime.datetime.now()

    client = Client(
        #user_uuid,
        clt_id,
        clt_name,
        clt_last_name,
        clt_email,
        clt_state,
        clt_city,
        clt_delivery_addres,
        user_created_data_timestamp,
        clt_orders
        )
    
 
    db.session.add(client)
    db.session.commit()
  

    return jsonify(client)


    #Crear un metodo para obtener las ordenes activas que tengas los usarios
