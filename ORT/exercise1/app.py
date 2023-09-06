from student_imp import Student
from instructor_imp import Instructor
from course_imp import Courses
from course_classroom_imp import CourseClassroom
import json

students_data = [[95851445,"Moises","moihernan@gmail.com",False],
                 [94323945,"Mariajose","mariaip@gmail.com",False]]

mydict = {}
list_of_object_students = [ mydict.update(sid) for sid, sname, semail, sscholarship in students_data]
print(list_of_object_students)

# list_of_object_students = [Student(user_id=sid, user_name=sname, user_mail=semail, student_scholarship=sscholarship)
#                             for sid, sname, semail, sscholarship in students_data]


# student1 = Student(1,"Kevin","kevlezama@gmail.com",False)
# print(student1)
# 
# course1 = Courses("A001BAF","Docker and Kubernets",100.00,"5 stars")
# print(course1)
# 
# instructor1 = Instructor(234,"Daminan", "D.gold@gmail.com", {})
# print(instructor1)
