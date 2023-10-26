from db_config import db
from models.instructor import Instructor


def get_all_instructors():

    instructors = Instructor.query.all()
    print(instructors)
