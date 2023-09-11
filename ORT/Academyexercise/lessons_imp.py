from dataclasses import dataclass
from datetime import time

class CoursesLessons:

    id_course_related: int
    lesson_name_plan: []
    lesson_time_duration: time
    lesson_time: str



cl = CoursesLessons(['Introdution'], time(minute=30), 'video')

cl.lesson_name_plan

print(cl)