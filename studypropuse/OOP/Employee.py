class Employee:
    def __init__(self,
                 employee_name,
                 employee_last_name,
                 employee_dni,
                 employee_phone,
                 employee_contract_type,
                 employee_credential_number,
                 employee_start_contract_date,
                 employee_end_contract_date = None
                 ):
        self.employee_name = employee_name
        self.employee_last_name = employee_last_name
        self.employee_dni = employee_dni
        self.employee_phone = employee_phone
        self.employee_contract_type = employee_contract_type
        self.employee_start_contract_date = employee_start_contract_date
        self.employee_end_contract_date = employee_end_contract_date
        self.employee_credential_number = employee_credential_number

    def show_employee_data(self):
        return '***Employee data***' \
               'Name: {}\n' \
               'Lastname: {}\n' \
               'DNI: {}\n' \
               'Contract type: {}\n' \
               'Contract number: {}\n' \
               'Start Contract date: {}\n' \
               'End Contract date: {}\n' \

class Administraive(Employee):

    def __init__(self,administrative_salary):
        self.administrative_salary = administrative_salary
        super().__init__()


if __name__ == '__main__':

    secretary1 = Administraive('Jeffrey',
                               'Bezitos',
                               1294214012,
                               12324343,
                               'TEMP',
                               'T698893',
                               '2022/01/20')

    print(secretary1.show_employee_data())