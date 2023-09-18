from dataclasses import dataclass
from datetime import time
from course_imp import Courses

class CoursesLessons:

    course_id_related: Courses.get_course_id
    lesson_name_plan: {any}
    lesson_time_duration: time
    lesson_type: str

    def __str__(self) -> str:
        nl = '\n'
        print(f'Course related: {self.course_id_related}{nl}, Lesson:{self.lesson_name_plan}{nl}, Duration:{self.lesson_time_duration}{nl}, Type: {self.lesson_type}')


course1 = Courses("A001BAF","Docker and Kubernets",100.00,"5 stars",[])
print(course1)

cl = (course1.get_course_id, {"Introduction": "What is Docker?"}, time(hour=1, minute=30),"V")
print(cl)