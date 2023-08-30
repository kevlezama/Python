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