from django.shortcuts import get_object_or_404
from users.models import User
from rest_framework.authtoken.models import Token


def create_user(
    username,
    first_name,
    last_name,
    email,
    birthday,
    password
):
    user = User(
        username=username,
        first_name=first_name,
        last_name=last_name,
        email=email,
        birthday=birthday
    )
    user.set_password(password)
    user.save()

    return user


def create_token(user):
    return Token.objects.create(user=user)


def get_user_by_id(user_id):
    return get_object_or_404(User, user_id)