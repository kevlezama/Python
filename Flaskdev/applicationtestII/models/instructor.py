from db_config import db
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from .course import Course

from typing import Optional, List

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
        nullable=False,
        unique=True)
    
    instructor_name: Mapped[str]
    instructor_middle_name: Mapped[str] 
    instructor_last_name: Mapped[str]
    instructor_full_name: Mapped[Optional [str]]
    instructor_owned_courses: Mapped[Optional[List["Course"]]] = relationship(back_populates="course_instrutor")

    def __init__(
            self,
            instructor_uid: uuid,
            instructor_id: int,
            instructor_name: str,
            instructor_middle_name: str,
            instructor_last_name: str,
            instructor_full_name: str = None,
            instructor_owned_courses: iter = [] ) -> None:

        self.instructor_uid = instructor_uid
        self.instructor_id = instructor_id
        self.instructor_name = instructor_name
        self.instructor_middle_name = instructor_middle_name
        self.instructor_last_name = instructor_last_name
        self.instructor_full_name = instructor_full_name
        self.instructor_owned_courses = instructor_owned_courses


        



