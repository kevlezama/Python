from imp_classes.StudentImp import *
from imp_classes.TeacherImp import *
from imp_classes.employees_imp.AdministrativeImp import *
if __name__ == "__main__":

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

    print(x)


