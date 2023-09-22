from db_config import db

from sqlalchemy import ForeignKey
from sqlalchemy import String
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column


class Student(db.Model):

    __tablename__ = 'students'

    student_id: Mapped[int] = mapped_column(primary_key=True)
    studet_name: Mapped[str] = mapped_column(String(30))
