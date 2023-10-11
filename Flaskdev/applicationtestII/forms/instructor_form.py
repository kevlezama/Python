from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SubmitField
from wtforms.validators import DataRequired

class InstructorForm(FlaskForm):

    instructor_id = IntegerField("Identification Number ID: ", validators=[DataRequired()])
    instructor_name = StringField('Instructor Name: ', validators=[DataRequired()])
    instructor_middle_name = StringField('Instructor Middle name: ', validators=[DataRequired()])
    instructor_last_name = StringField('Instructor Lastname: ', validators=[DataRequired()])
    submit = SubmitField('Submit')

    