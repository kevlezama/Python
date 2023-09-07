from user_imp import Users
from course_imp import Courses
import json
class Instructor(Users):

    def __init__(
            self,
            user_id: int,
            user_name: str,
            user_mail: str,
            instructor_owned_coruses_id: list
            ) -> None:
        super().__init__(user_id, user_name, user_mail)
        
        self.instructor_owned_coruses_id = instructor_owned_coruses_id

    def __repr__(self) -> str:
        nl = '\n'
        return f"{__class__.__name__}:{nl} ID: {self.user_id}{nl} Name: {self.user_name}{nl} Mail: {self.user_mail}{nl} OwnedCourses:{nl}{self.instructor_owned_coruses_id}"

    @property
    def get_instructor_owned_coruses_id(self) -> any:

        if self.instructor_owned_coruses_id == [] or self.instructor_owned_coruses_id == "":
            return "There is not courses own by this user."
        else:
            return self.instructor_owned_coruses_id
    
    @get_instructor_owned_coruses_id.setter
    def set_instructor_owned_coruses_id(self, new_courses_classroom:str):
        
        self.instructor_owned_coruses_id.append(new_courses_classroom)
        return self.instructor_owned_coruses_id
    

    def get_instructor_full_description(self):
        """_summary_

        Returns:
            _type_: _description_
        """
        use_json_ftm = json.dumps(self.__dict__ , indent=4)
        return use_json_ftm

