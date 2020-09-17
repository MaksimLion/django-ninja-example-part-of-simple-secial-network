from typing import List
from ninja import Router
from base.auth import auth
from .models import User
from .schemas import UserRequestSchema, UsersListResponseSchema, UserCreateResponseSchema
from .services import create_user, create_token, get_user_by_id


router = Router()


@router.get("/", response=List[UsersListResponseSchema], auth=auth)
def users_list(request):
    return User.objects.all()


@router.get("/{user_id}")
def user_detail(request, user_id):
    pass


@router.post("/", response=UserCreateResponseSchema)
def user_create(request, user: UserRequestSchema):
    user = create_user(
        user.username,
        user.first_name,
        user.last_name,
        user.email,
        user.birthday,
        user.password
    )
    token = create_token(user)
    user.token = token.key
    return user
