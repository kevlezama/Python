import json
from datetime import time

class Courses:

    def __init__(
            self,
            course_id: str,
            course_title: str,
            course_price: float,
            course_rank: str,
            course_lessons: list
        ) -> None:
        self.course_id = course_id
        self.course_title = course_title
        self.course_price = course_price
        self.course_rank = course_rank
        self.course_lessons = course_lessons

    def __repr__(self) -> str:
        nl = '\n'
        return f"{__class__.__name__}:{nl} ID: {self.course_id}{nl} Course Title: {self.course_title}{nl} Course Price: {self.course_price}{nl} Rank: {self.course_rank}{nl} Lessons:{self.course_lessons}"

    def get_json_format(self):
        use_json_ftm = json.dumps(self.__dict__ , indent=4)
        return use_json_ftm
    
    @property
    def get_course_id(self):
        return self.course_id
    
    @get_course_id.setter
    def get_course_id(self, set_new_course_id):
        self.course_id = set_new_course_id
        return self.course_id
    
    @property
    def get_course_title(self):
        return self.course_title
    
    @get_course_title.setter
    def get_course_title(self, set_new_course_title):
        self.course_title = set_new_course_title
        return self.course_title
    
    @property
    def get_course_price(self):
        return self.course_price
    
    @get_course_price.setter
    def get_course_price(self, set_new_course_price):
        self.course_price = set_new_course_price
        return self.course_price
    
    @property
    def get_course_rank(self):
        return self.get_course_rank
    
    @get_course_rank.setter
    def get_course_rank(self, set_new_course_rank):
        self.course_id = set_new_course_rank
        return self.course_id
    

#    def get_courses_lessons(self, cl: CoursesLessons):
#        
#        course_lessons_dict = dict.fromkeys( )
#        return course_lessons_dict


class CoursesLessons:

    course_id_related: Courses.get_course_id
    lesson_name_plan: {}
    lesson_time_duration: time
    lesson_type: str


course1 = Courses("A001BAF","Docker and Kubernets",100.00,"5 stars",[])
print(course1)

cl = (course1.get_course_id, {"Introduction": "What is Docker?"}, time(hour=1, minute=30),"V")

# Falta agregar get_lessosns en la clase courses y que las enumere por titulo 

