from abstract_classes.Person import *

class Student(Person):

    def __init__(self, p_first_name: str,
                    p_middle_name: str,
                    p_last_name: str,
                    p_dni: int,
                    p_personal_phone:int,
                    p_address:str,
                    student_grade: str,
                    student_seccion: str,
                    student_level: str) -> None:
        super().__init__(p_first_name,
                        p_middle_name, 
                        p_last_name,
                        p_dni,
                        p_personal_phone,
                        p_address)
        self.student_grade = student_grade
        self.student_seccion = student_seccion
        self.student_level = student_level

    def get_person_basic_details(self):
        pass
    
    def __repr__(self) -> str:
        return (f"{self.__class__.__name__}: {self.student_grade}, {self.student_seccion}, {self.student_level}")
