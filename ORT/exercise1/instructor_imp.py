from user_imp import Users

class Instructor(Users):

    def __init__(
            self,
            user_id: int,
            user_name: str,
            user_mail: str,
            instructor_current_courses_classroom: dict) -> None:
        super().__init__(user_id, user_name, user_mail)
        
        self.teacher_owned_courses = instructor_current_courses_classroom

    def __repr__(self) -> str:
        nl = '\n'
        return f"{__class__.__name__}:{nl} ID: {self.user_id}{nl} Name: {self.user_name}{nl} Mail: {self.user_mail}{nl} CurrentClassrooms:{nl}{self.teacher_owned_courses}"
    