import course_imp

class Categories():

    def __init__(
            self,
            category_id: int,
            category_name: str,
            courses_related: course_imp
        ) -> None:
        self.category_id = category_id
        self.category_name = category_name
        self.courses_related = courses_related

        
