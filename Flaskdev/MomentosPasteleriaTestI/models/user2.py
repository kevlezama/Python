from app import db
from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column, relationship
import uuid
import datetime

class User(db.Model):

    __tablename__ = 'user_model'

    user_uid: Mapped[uuid.UUID] = mapped_column(
        init=False,
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