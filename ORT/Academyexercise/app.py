from student_imp import Student
from instructor_imp import Instructor
from course_imp import Courses
from categories_imp import Categories
from course_classroom_imp import CourseClassroom


# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
# '''
# Genereate objects iterating a list with data
# '''
# students_data = [[95851445,"Moises","moihernan@gmail.com",False],
#                  [94323945,"Mariajose","mariaip@gmail.com",False]]
# 
# list_of_object_students = [[Student(user_id=sid, user_name=sname, user_mail=semail, student_scholarship=sscholarship)]
#                              for sid, sname, semail, sscholarship in students_data]
# 
# print(list_of_object_students)
# 
# for student_obj_list in list_of_object_students:
#     for student_obj in student_obj_list:
#         print(type(student_obj))
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

student1 = Student(1,"Kevin","kevlezama@gmail.com",False)
# print(student1)

course1 = Courses("A001BAF","Docker and Kubernets",100.00,"5 stars",[])
course2 = Courses("C000354","Haskell",600.00,"5 stars",[])
# print(course1)

category1 = Categories("IT0001","IT - Information and Technology", [])


instructor1 = Instructor(234,"Daminan", "D.gold@gmail.com", [])
print(instructor1.get_instructor_full_description())
instructor1.set_instructor_owned_coruses_id = course1.course_id
print(instructor1.get_instructor_full_description())
instructor1.set_instructor_owned_coruses_id = course2.course_id
print(instructor1.get_instructor_full_description())


# courseclass = CourseClassroom(1344, student1, instructor1, course1, "IT:TECH")


