from datetime import datetime
from ninja import Schema
from typing import List
from users.schemas import UsersListResponseSchema


class MessageRequestSchema(Schema):
    text: str


class MessageResponseSchema(Schema):
    to_dialog_id: int
    datetime: datetime
    from_user_id: int
    text: str
    is_my_message: bool


class MessageFilters(Schema):
    my: bool = False
    q: str = None


class DialogSchema(Schema):
    id: int
    users: List[UsersListResponseSchema]
    messages: List[MessageResponseSchema]


class CreateDialogSchema(Schema):
    users: List[int]
