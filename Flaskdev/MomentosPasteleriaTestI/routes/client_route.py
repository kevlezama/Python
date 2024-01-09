
# Flask framework
from flask import Blueprint, request, jsonify, make_response

# Sqlalchemy ORM API
from sqlalchemy import select

# Application packages
from app import db
from models.client import Client

# Python buildin 
import uuid
import datetime
import json


client_route  = Blueprint('clients' ,__name__)

CLIENTS_ORDER_BY_CLIENT_ID_STM = select(Client).order_by(Client.client_id)

@client_route.route('/clients/getall/clients', methods=['GET'])
def get_all_clients():
    query_execution = db.session.execute(CLIENTS_ORDER_BY_CLIENT_ID_STM).all()
    #clients = Client.query.all()
    #with db.session as session:
    #    for row in session.execute(CLIENTS_ORDER_BY_CLIENT_ID_STM):
    #        print(row)
    #return clients
    return query_execution

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

    CLIENTS_ORDER_BY_CLIENT_ID_STM.where(Client.client_email)

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

    return jsonify(client), 200

    #Crear un metodo para obtener las ordenes activas que tengas los usarios
