from app import create_app
from models.students import Student
from db_config import db

applicationtestII = create_app()

if __name__ == "__main__":

    with applicationtestII.app_context():
        
        student1 = Student(1, 'Kevin')
        db.session.add(student1)
        db.session.commit()
        db.session.close()

    applicationtestII.run(debug=True)


