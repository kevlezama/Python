from abstract_classes import Person


class Student(Person):
    def __init__(self, student_name, student_last_name, student_dni, student_age, student_birthday):
        self.student_name = student_name
        self.s_last_name = student_last_name
        self.s_dni = student_dni
        self.s_age = student_age
        self.s_birthday = student_birthday

    def get_full_student_data(self):
        return self.student_name