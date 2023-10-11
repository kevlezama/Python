from flask import Blueprint, render_template, redirect

from app import db

from forms.instructor_form import InstructorForm

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

    #instr_data =[]
    #if instructor_form.validate_on_submit():
        #instr_data.append(instructor_form.instructor_id.data)
        #instr_data.append(instructor_form.instructor_name.data)
        #instr_data.append(instructor_form.instructor_middle_name.data)
        #instr_data.append(instructor_form.instructor_last_name.data)
        #return redirect("instructor_form_reply.html",)
    
