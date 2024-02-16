from dbconfig import db
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from models.client import Client
    
from sqlalchemy import select

stm = select(Client).order_by(Client.client_id).where(Client.client_email=="mimix@gmail.com")
query = db.session.execute(stm).first()
print(query)