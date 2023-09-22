from db_config import db

from sqlalchemy import ForeignKey
from sqlalchemy import String
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy import Uuid

class Instructor(db.Model):

    __tablename__ = 'instructor'

    instructor_uid: Mapped[Uuid.uuid4()] = mapped_column(
        primary_key=True,
        nullable=False)
    
    instructor_id: Mapped[int] = mapped_column(
        primary_key=True,
        nullable=False)
    

