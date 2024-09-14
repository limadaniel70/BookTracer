class User:
    def __init__(
        self,name: str, email: str, phone: str, creation_date: str
    ) -> None:
        self.name = name
        self.email = email
        self.phone = phone
        self.creation_date = creation_date


class UserDTO:
    def __init__(self, id: int, name: str, creation_date: str) -> None:
        self.user_id: int = id
        self.name: str = name
        self.creation_date: str = creation_date
