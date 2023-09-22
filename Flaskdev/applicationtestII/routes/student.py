from flask import Blueprint, render_template


students = Blueprint('student' ,__name__)

@students.route('/students')
def get_all_studets() -> any:
    return render_template("students.html")
