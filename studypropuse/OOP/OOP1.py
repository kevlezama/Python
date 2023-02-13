class Student:
    def __init__(self, student_name,s_last_name,s_dni,s_age,s_birthday):
        
        self.student_name = student_name
        self.s_last_name = s_last_name
        self.s_dni = s_dni
        self.s_age = s_age
        self.s_birthday = s_birthday

    def get_full_student_data(self):
        return self.student_name

student1 = Student('Kevin','Lezama',95851445,28,'1995/26/01')

#fullStudentData = 

print(student1.get_full_student_data())




