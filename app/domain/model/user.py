from app.domain.model.entity import Entity
from app.domain.model.value import Value


class UserId(Value):
    def __init__(self, value: str) -> None:
        self.value = value


class Name(Value):
    def __init__(self, value: str) -> None:
        self.value = value


class Email(Value):
    def __init__(self, value: str) -> None:
        self.value = value


class User(Entity):
    def __init__(self,
                 user_id: UserId,
                 name: Name,
                 email: Email) -> None:
        self.user_id = user_id
        self.name = name
        self.email = email
