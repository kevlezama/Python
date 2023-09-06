import json

class Users():

    def __init__(
            self,
            user_id: int,
            user_name: str,
            user_mail: str,
            # user_scholarship: bool
        ) -> None:
        self.__user_id = user_id
        self.user_name = user_name
        self.user_mail = user_mail
        # self.user_scholarship = user_scholarship

    def __repr__(self) -> str:
        nl = '\n'
        return f"{__class__.__name__}:{nl} ID: {self.__user_id}{nl} Name: {self.user_name}{nl} Mail: {self.user_mail}{nl}"

    @property
    def user_id(self):
        return self.__user_id;

    @user_id.setter
    def user_id(self, set_new_user_id):
        print("Entering in the Setter")
        self.__user_id = set_new_user_id
        print(f'{__class__.__name__} has been modified')

    @property
    def get_user_name(self):
        return self.user_name
    
    @get_user_name.setter
    def get_user_name(self, set_new_user_name):
        self.user_name = set_new_user_name
        return self.user_name
    
    @property
    def get_user_mail(self):
        return self.user_mail

    @get_user_mail.setter
    def get_user_mail(self, set_new_user_mail):
        self.user_mail = set_new_user_mail
        return self.user_mail

#    @property
#    def get_user_scholarship(self):
#        return self.user_scholarship
#    
#    @get_user_scholarship.setter
#    def get_user_scholarship(self, set_new_user_scholarship):
#        self.user_scholarship = set_new_user_scholarship
#        return self.user_scholarship
        
    def get_json_format(self):
        use_json_ftm = json.dumps(self.__dict__ , indent=4)
        return use_json_ftm
