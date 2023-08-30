from abc import ABC, abstractmethod
from abstract_classes.Person import Person

class Employee(Person, ABC):

    def __init__(self, p_first_name: str,
                    p_middle_name: str,
                    p_last_name: str,
                    p_dni: int,
                    p_personal_phone: int,
                    p_address: str,
                    employee_salary: float,
                    employee_hire_date: str,
                    employee_marital_stauts: str) -> None:
        super().__init__(p_first_name,
                        p_middle_name, 
                        p_last_name,
                        p_dni,
                        p_personal_phone,
                        p_address)
        self.employee_salary = employee_salary
        self.employee_hire_date = employee_hire_date
        self.employee_marital_stauts = employee_marital_stauts

    def get_person_basic_details(self):
        pass
    
    @abstractmethod
    def paychecks(self):
        raise NotImplementedError
    
    @abstractmethod
    def get_actual_salary(self):
        raise NotImplementedError
    
'''class TeacherImp(Employee):

    def __init__(self, p_first_name: str,
                    p_middle_name: str,
                    p_last_name: str,
                    p_dni: int,
                    p_personal_phone: int,
                    p_address: str,
                    employee_salary: float,
                    employee_hire_date: str,
                    employee_marital_stauts: str,
                    teacher_subject_area: [],
                    teacher_actual_sub: [],
                    teacher_asigned_grades: [] ) -> None:
        super().__init__(p_first_name,
                        p_middle_name, 
                        p_last_name,
                        p_dni,
                        p_personal_phone,
                        p_address,
                        employee_salary,
                        employee_hire_date,
                        employee_marital_stauts)
        
        self.teacher_subject_area = teacher_subject_area
        self.teacher_actual_sub =  teacher_actual_sub
        self.teacher_asigned_grades = teacher_asigned_grades
        
    def paychecks(self):
        pass

    def get_actual_salary(self):
        pass

x = TeacherImp("Sergio",
             "Antonio",
             "Lezama",
             6498760,
             4142497260,
             "Altamira",
             3534.34,
             "1995/07/10",
             "Single",
             ['Mathematics','Physics'],
             ['Mathematics'],
             ['4to','5to'])

print(x)'''



        
