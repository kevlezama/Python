# Flask framework
from flask import Flask
from flask_migrate import Migrate

# Project config files
from db_config import db

# Routes
from routes.index import index
from routes.student import students

def create_app():

    app = Flask(__name__)
    app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql+psycopg2://postgres:admin@localhost/applicationtestii"
    app.config["SQLALCHEMY_ECHO"] = True
    app.config["SQLALCHEMY_RECORD_QUERIES"] = True
    db.init_app(app)
    # migrate = Migrate(app, db)
    from models.students import Student
    from models.course import Course
    from models.instructor import Instructor
    app.register_blueprint(index)
    app.register_blueprint(students)
    with app.app_context():
        db.drop_all()
        db.create_all()
        print('Created Database!')
    
    return app


