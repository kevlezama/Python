from config.dbconfig import db
from typing import Optional, List
from sqlalchemy import String, Integer, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
import uuid
import datetime

class User(db.Model):

    __tablename__ = 'user_model'

    user_uid: Mapped[uuid.UUID] = mapped_column(
        primary_key=True,
        nullable=False,
        default=uuid.uuid4)
    
    user_id: Mapped[int] = mapped_column(
        unique=True)
    
    user_name: Mapped[str] = mapped_column(
        String(15)
    )

    user_last_name: Mapped[str] = mapped_column(
        String(20)
    )

    user_tier_rank: Mapped[str]
    user_paid: Mapped[bool]
    user_free: Mapped[bool]
    user_created_timestamp: Mapped[datetime.datetime]
    
    def __init__(
            self,
            user_uid: uuid,
            user_id: int,
            user_name: str,
            user_last_name: str,
            user_tier_rank: str,
            user_paid:bool,
            user_free:bool,
            user_created_timestamp: datetime) -> None:

        self.user_uid = user_uid
        self.user_id = user_id
        self.user_name = user_name
        self.user_last_name = user_last_name
        self.user_tier_rank = user_tier_rank
        self.user_paid = user_paid
        self.user_free = user_free
        self.user_created_timestamp = user_created_timestamp


    def __repr__(self) -> str:
        return f'<User: {self.user_id}, {self.user_name}, {self.user_last_name}>'

