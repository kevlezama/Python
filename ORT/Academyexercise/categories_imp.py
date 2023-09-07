from course_imp import Courses

class Categories():

    def __init__(
            self,
            category_id: int,
            category_name: str,
            courses_available_for_catergoty: list
        ) -> None:
        self.category_id = category_id
        self.category_name = category_name
        self.courses_available_for_catergoty = courses_available_for_catergoty




        
