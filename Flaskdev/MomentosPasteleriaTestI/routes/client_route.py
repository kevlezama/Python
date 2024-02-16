# Flask framework
from flask import Blueprint, request, jsonify
# Sqlalchemy ORM API
from sqlalchemy import select
from sqlalchemy.exc import NoResultFound, MultipleResultsFound

# Application packages
from app import db
from models.client import Client

# Python buildin 
import uuid
import datetime
import json
import logging

FORMAT = '%(asctime)s - %(levelname)s - %(message)s'
FILE = "basic.log"

logging.basicConfig(
        level=logging.INFO,
        format=FORMAT,
        datefmt="%Y-%m-%d %H:%M:%S",
        filename=FILE
    )
    
client_route  = Blueprint('clients', __name__)

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

@client_route.route('/clients/v2/createclient', methods=['POST'])
def create_new_client_v2() -> any:

    request_data = request.get_json()
    clt_email = request_data['client_email']

    get_client_email = db.session.query(Client).filter(Client.client_email==clt_email)
    logging.info('-------------- START HERE ------------------')
    logging.info(get_client_email)
    return {}
    '''try:
        search_if_client_email_exists = db.session.execute(get_client_email).first()

    
    except MultipleResultsFound as e:

        return e'''

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
    clt_addrs = {}
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
        clt_orders,
        clt_addrs
        )
    
    db.session.add(client)
    db.session.commit()

    return jsonify(client), 200