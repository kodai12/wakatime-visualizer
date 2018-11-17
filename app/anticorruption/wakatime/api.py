from app.domain.model.user import User
from app.domain.factory.user import create_user


class WakatimeUserTranslator:
    def __init__(self, user_dict: dict) -> None:
        self.user_dict = user_dict["data"]

    def to_my_user(self) -> User:
        return create_user(
            user_id=self.user_dict["id"],
            name=self.user_dict["display_name"],
            email=self.user_dict["email"],
        )
