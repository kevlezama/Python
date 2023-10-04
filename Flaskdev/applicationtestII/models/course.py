from db_config import db

from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from .instructor import Instructor

from typing import Optional, List


from sqlalchemy import Uuid,ForeignKey, String, DateTime
from sqlalchemy.orm import Mapped, mapped_column, relationship

import uuid
from datetime import datetime

class Course(db.Model):
    
    __tablename__ = 'courses'

    course_uid: Mapped[uuid.UUID] = mapped_column(
        primary_key=True,
        nullable=False,
        default=uuid.uuid4)
    
    #course_create_dt: Mapped[DateTime] = mapped_column(default=datetime)

    course_title: Mapped[str]
    course_price: Mapped[float] = mapped_column(default=0.0)
    course_rank: Mapped[str] = mapped_column(default=0)
    course_instrcutor_id: Mapped[uuid.UUID] = mapped_column(ForeignKey("instructor.instructor_uid"), unique=True)
    course_instrutor: Mapped[List["Instructor"]] = relationship(back_populates="instructor_owned_courses")

