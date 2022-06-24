import typing
from pydantic import BaseModel


class User(BaseModel):
    first_name: str
    last_name: str
    username: str
    email: str
    password: str

    class Config:
        arbitrary_types_allowed = True

    def update(self, **mapping: typing.Dict):
        return self.copy(update=mapping)


def user_factory(
    first_name: str,
    last_name: str,
    username: str,
    email: str,
    password: str,
) -> User:
    return User(
        first_name=first_name,
        last_name=last_name,
        username=username,
        email=email,
        password=password,
    )
