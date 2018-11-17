from app.domain.model.user import UserId
from app.domain.model.user import Name
from app.domain.model.user import Email
from app.domain.model.user import User

def create_user(user_id: str,
                name: str,
                email: str) -> User:
    return User(
        user_id=UserId(user_id),
        name=Name(name),
        email=Email(email)
    )

