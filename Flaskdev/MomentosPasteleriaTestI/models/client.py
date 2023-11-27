from app import db
from typing import Optional, Dict
from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column, relationship, attribute_keyed_dict

from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from .orders import Orders

import uuid
import datetime

class Client(db.Model):

    DATETIME = datetime.datetime.now()

    __tablename__ = 'client_model'

    client_uid: Mapped[uuid.UUID] = mapped_column(
        init=False,
        primary_key=True,
        nullable=False,
        default=uuid.uuid4)
    
    client_id: Mapped[int] = mapped_column(
        unique=True)
    
    client_name: Mapped[str] = mapped_column(
        String(15)
    )

    client_last_name: Mapped[str] = mapped_column(
        String(20)
    )

    client_email: Mapped[str] = mapped_column(
        String(30)
    )

    client_state:Mapped[str]
    client_city: Mapped[str]
    client_delivery_address: Mapped[str]
    client_created_timestamp: Mapped[datetime.datetime] = mapped_column (
        insert_default=datetime.datetime.now
    )

    # Relationship with order model
    orders: Mapped[Optional[Dict[str,"Orders"]]]= relationship(
        collection_class=attribute_keyed_dict("order_uid"),
        cascade="all, delete-orphan", back_populates='clients')
