from app import create_app
from models.students import Student
from models.instructor import Instructor
from db_config import db

applicationtestII = create_app()

if __name__ == "__main__":

    # with applicationtestII.app_context():
        # instructor1 = Instructor('4b5705e8-71bf-40b5-bab3-da5fe3cc2ba9',
        #                         95851445,
        #                         'Kevin',
        #                         'Omar',
        #                         'Lezama',
        #                         'Kevin Omar Lezama Pina', [])
        #
        # db.session.add(instructor1)
        # db.session.commit()
        # db.session.close()

    applicationtestII.run(debug=True)

    # with applicationtestII.app_context():

    #    instructors = Instructor.query.all()
    #    print(instructors)
    #    instructor_name_list = [instructor.instructor_name for instructor in instructors]
    #    print(instructor_name_list)
