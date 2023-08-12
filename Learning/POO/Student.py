
from abc import ABC, abstractmethod

class Person(ABC):
    
    def __init__(self, p_first_name: str, p_middle_name: str, p_last_name: str, p_dni: int,
                  p_personal_phone:int ,p_address:str) -> None:
        self.p_first_name = p_first_name
        self.p_middle_name = p_middle_name
        self.p_last_name = p_last_name
        self.p_dni = p_dni
        self.p_address = p_address
        self.p_personal_phone = p_personal_phone

    @abstractmethod
    def get_person_basic_details(self):
        raise NotImplementedError


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
        
kevin = Student("Kevin",
                "Omar",
                "Lezama",
                95851445,
                1133044363,
                "Av coronel niceto vega 5658",
                "4to",
                "A",
                "Secundario")
# kevin = Student("")

print(kevin)