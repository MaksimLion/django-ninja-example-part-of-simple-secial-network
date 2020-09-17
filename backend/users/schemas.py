from datetime import date
from ninja import Schema

from users.models import User


class UserRequestSchema(Schema):
    first_name: str
    last_name: str
    email: str
    username: str
    birthday: date
    password: str


class UserCreateResponseSchema(UserRequestSchema):
    token: str


class UsersListResponseSchema(Schema):
    id: int
    username: str
