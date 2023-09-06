from user_imp import Users
import json

class Student(Users):
    def __init__(self, user_id: int, user_name: str, user_mail: str, student_scholarship: bool) -> None:
        super().__init__(user_id, user_name, user_mail)

        self.student_scholarship = student_scholarship

    def __repr__(self) -> str:
        nl = '\n'
        return f"{__class__.__name__}:{nl} ID: {self.user_id}{nl} Name: {self.user_name}{nl} Mail: {self.user_mail}{nl} Scholarship: {self.student_scholarship}"

    
    def get_json_format(self):
        use_json_ftm = json.dumps(self.__dict__ , indent=4)
        return use_json_ftm

    
    def build_student_obj(student_date: dict):
        pass
        

