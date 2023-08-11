from abstract_classes import Person

class Person_imp(Person):
    
    def __init__(self, p_first_name, p_last_name, p_dni,
                  p_personal_phone:int = None, p_middle_name = None,p_address = None):
        super.__init__()
        self.p_first_name = p_first_name
        self.p_middle_name = p_middle_name
        self.p_last_name = p_last_name
        self.p_dni = p_dni
        self.p_address = p_address
        self.p_personal_phone = p_personal_phone

    def get_person_basic_details(self):

        return f"Basic details:\n Name: {self.p_first_name}\n Lastname: {self.p_last_name}\n DNI: {self.p_dni}"
    
    def get_report(self):
        pass

    def __repr__(self) -> str:
        ## __class__ return class format name. __class__.___name___ return class str name
        return f"{self.__class__}(Name={self.p_first_name}) " f" {self.__class__. __name__}(Name={self.p_first_name})"

if __name__ == '__main__':
    
    try:
        x = Person("Kevin","Lezama",95851445)
        y = Person("Mariajose","Ibarra","96756123")
        print(x)
        print(y)
    except Exception as e:
        print(f"Unexpected {e=}, {type(e)=}")

people = {95851445:["Kevin","Lezama"], 97436212:["Valeria","Abad"]}

'''rslt = [Person(arg1,arg2,arg3) for arg1 in people[95851445]]'''



