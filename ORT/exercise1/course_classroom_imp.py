from student_imp import Student
from instructor_imp import Instructor
from course_imp import Courses

class CourseClassroom:
    def __init__(self, cc_student: Student, cc_teacher: Instructor, cc_course: Courses, cc_type: str) -> None:
        self.cc_student = cc_student
        self.cc_teacher = cc_teacher
        self.cc_course = cc_course
        self.cc_type = cc_type

    def __repr__(self) -> str:
        nl = '\n'
        return f"{__class__.__name__}:{nl} ID: {self.cc_student}{nl} Name: {self.cc_teacher}{nl} Mail: {self.cc_course}{nl}"
    

