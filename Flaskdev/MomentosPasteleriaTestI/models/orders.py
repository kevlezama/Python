from app import db
from typing import Optional, List, Dict
from sqlalchemy import String, Integer, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship, attribute_keyed_dict

from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from .items import Items
    from .client import Client



import uuid
import datetime

class Orders(db.Model):

    ######## Mapped columns in DB ############

    __tablename__ = 'orders_model'

    order_uid: Mapped[uuid.UUID] = mapped_column(
        init=False,
        primary_key=True,
        nullable=False,
        default=uuid.uuid4)
    
    order_id: Mapped[int] = mapped_column(
        unique=True)
    
    order_status: Mapped[bool]
    order_simple_date: Mapped[datetime.date]
    order_created_date: Mapped[datetime.datetime]
    order_client_uid: Mapped[uuid.UUID] = mapped_column(ForeignKey("client_model.client_uid"))

    ########### Relationships ##########

    # Relationship with client model
    clients: Mapped["Client"] = relationship(back_populates="orders")

    # Relationship with item model
    #items: Mapped[List["Items"]] = relationship(back_populates="order")

    #items: Mapped[Optional[Dict[str,"Items"]]]= relationship(
    #    collection_class=attribute_keyed_dict("item_uid"),
    #    cascade="all, delete-orphan",back_populates="order")
    
    def order_get_id_prefix(self):

        self.order_id = 0000000000
        self.order_id+=1

        self.order_id = "MP-O-" + str(self.order_id)
