import categories_imp
import user_imp

class Courses():

    def __init__(
            self,
            course_id: str,
            course_title: str,
            course_price: float,
            course_rank: str,
            couse_owner: []
        ) -> None:
        self.course_id = course_id
        self.course_title = course_title
        self.course_price = course_price
        self.course_rank = course_rank
        self.course_owner = couse_owner

    def __repr__(self) -> str:
        nl = '\n'
        return f"{__class__.__name__}:{nl} ID: {self.course_id}{nl} Course Title: {self.course_title}{nl} Course Price: {self.course_price}{nl} Course Rank: {self.course_rank}{nl} Course Owner:{nl}{self.course_owner}"

