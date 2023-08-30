from flask import Blueprint, render_template

students = Blueprint('students' ,__name__)

@students.route('/students')
def home() -> any:
    return render_template("students.html")

@students.route('/students/1er')
def home() -> any:
    return render_template("students.html")