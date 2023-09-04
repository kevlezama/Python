class Users():

    def __init__(
            self,
            user_id: int,
            user_name: str,
            user_mail: str,
            user_scholarship: bool
        ) -> None:
        self.user_id = user_id
        self.user_name = user_name
        self.user_mail = user_mail
        self.user_scholarship = user_scholarship

    def __repr__(self) -> str:
        nl = '\n'
        return f"{__class__.__name__}:{nl} ID: {self.user_id}{nl} Name: {self.user_name}{nl} Mail: {self.user_mail}{nl} Scholarship: {self.user_scholarship}"

