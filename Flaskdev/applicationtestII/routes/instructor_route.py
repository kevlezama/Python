from flask import Blueprint, render_template

from app import db


instructor_route = Blueprint('instructor' ,__name__)

@instructor_route.route('/instructor')
def get_all_instructors() -> any:
    return render_template("instructor.html", title='Instructors')
