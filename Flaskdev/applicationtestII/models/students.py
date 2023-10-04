from db_config import db

from sqlalchemy import ForeignKey
from sqlalchemy import String
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column


# Python build-int

import uuid



class Student(db.Model):

    __tablename__ = 'students'

    course_uid: Mapped[uuid.UUID] = mapped_column(
        primary_key=True,
        nullable=False,
        default=uuid.uuid4)  

    student_id: Mapped[int] = mapped_column(primary_key=True)

    studet_name: Mapped[str] = mapped_column(String(30))
