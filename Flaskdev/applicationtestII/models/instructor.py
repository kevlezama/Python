from db_config import db
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from .course import Course

from typing import Optional, List

# from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy import Uuid, String, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
import uuid


class Instructor(db.Model):

    __tablename__ = 'instructor'

    instructor_uid: Mapped[uuid.UUID] = mapped_column(
        primary_key=True,
        nullable=False,
        default=uuid.uuid4)
    
    instructor_id: Mapped[int] = mapped_column(
        primary_key=True,
        nullable=False)
    
    instructor_name: Mapped[str]
    instructor_middle_name: Mapped[str] 
    instructor_last_name: Mapped[str]
    instructor_full_name: Mapped[Optional [str]]
    instructor_owned_courses: Mapped[Optional[List["Course"]]] = relationship(back_populates="course_instrutor")



