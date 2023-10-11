from flask import Blueprint, render_template

from app import db


courses_route = Blueprint('courses' ,__name__)

@courses_route.route('/courses')
def get_all_courses() -> any:
    return render_template("courses.html", title='Courses')
