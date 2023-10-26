from app import create_app
from models.students import Student
from models.instructor import Instructor
from db_config import db

applicationtestII = create_app()

if __name__ == "__main__":

    applicationtestII.run(debug=True)

    # with applicationtestII.app_context():

    #    instructors = Instructor.query.all()
    #    print(instructors)
    #    instructor_name_list = [instructor.instructor_name for instructor in instructors]
    #    print(instructor_name_list)
