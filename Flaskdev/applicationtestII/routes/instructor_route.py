from flask import Blueprint, render_template, redirect
from app import db
from models.instructor import Instructor
from forms.instructor_form import InstructorForm
import uuid

from sqlalchemy import select

instructor_route = Blueprint('instructor' ,__name__)

@instructor_route.route('/instructor')
def get_all_instructors() -> any:
    return render_template("instructor.html", title='Instructors')

@instructor_route.route('/instructor/instructor_form', methods=['GET', 'POST'])
def get_form_instructor() -> any:

    instructor_form = InstructorForm()
    instr_data =[]
    if instructor_form.validate_on_submit():
        instr_data.append(instructor_form.instructor_name.data)
        return render_template("instructor_form_reply.html", data=instr_data)
    return render_template("instructor_form.html", title='Instructors', form =instructor_form)


@instructor_route.route('/instructor/add_instructor', methods=['GET', 'POST'])
def create_instructor() -> any:

    ins_uuid = uuid.uuid4()

    instructor_form = InstructorForm()
    if instructor_form.validate_on_submit():

        ins_id = instructor_form.instructor_id.data
        ins_name = instructor_form.instructor_name.data
        ins_mid_name = instructor_form.instructor_middle_name.data
        ins_last_name = instructor_form.instructor_last_name.data
        
        try:

            instructor = Instructor(ins_uuid, ins_id, ins_name, ins_mid_name, ins_last_name)
            db.session.add(instructor)
            db.session.commit()
            db.session.close()
            return render_template("instructor_created_successfully.html")

        except Exception as e:
            print(e)

    return render_template("instructor_form.html", title='Instructors', form =instructor_form)


@instructor_route.route('/instructor/all_instructors', methods=['GET', 'POST'])
def get_all_instructorsv1() -> any:
    instructors = Instructor.query.all()

    return render_template('instructor.html', instructors=instructors)




