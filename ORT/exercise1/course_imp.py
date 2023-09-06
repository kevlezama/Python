import json

class Courses():

    def __init__(
            self,
            course_id: str,
            course_title: str,
            course_price: float,
            course_rank: str
        ) -> None:
        self.course_id = course_id
        self.course_title = course_title
        self.course_price = course_price
        self.course_rank = course_rank

    def __repr__(self) -> str:
        nl = '\n'
        return f"{__class__.__name__}:{nl} ID: {self.course_id}{nl} Course Title: {self.course_title}{nl} Course Price: {self.course_price}{nl}"

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
    

        