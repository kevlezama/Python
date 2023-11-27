from app import db
from sqlalchemy.orm import Mapped, mapped_column,relationship
from typing import Optional
import datetime
import uuid

from sqlalchemy import func

from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from .orders import Orders

class Items(db.Model):

    __tablename__ = 'items_model'

    item_uid: Mapped[uuid.UUID] = mapped_column(
        init=False,
        primary_key=True,
        nullable=False,
        default=uuid.uuid4)
    
    item_id: Mapped[int] = mapped_column(
        init=False,
        unique=True,
        insert_default=func.item_get_id_prefix())
    
    item_name: Mapped[str]
    item_price: Mapped[float]
    item_availability: Mapped[bool]
    item_created_date: Mapped[datetime.datetime] = mapped_column (
        insert_default=datetime.datetime.now
    )

    #order: Mapped[Optional["Orders"]] = relationship(back_populates="items", primaryjoin="Orders.items")
    
    def obj_to_dict(self):

        data_request ={

            "item_uid":self.item_uid,
            "item_id":self.item_id,
            "item_code":self.item_name,
            "item_name":self.item_price,
            "item_price":self.item_price,
            "item_availability":self.item_availability,
            "item_created_date":str(self.item_created_date)
        }

        return data_request
    
    def item_get_id_prefix(self):

        rslt = self.item_id + 1

        return rslt