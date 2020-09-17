from django.contrib.auth.hashers import check_password
from django.http import Http404
from django.shortcuts import get_object_or_404
from rest_framework.authtoken.models import Token
from users.models import User


def check_user_credentials(email, password):
    user = get_object_or_404(User, email=email)
    if check_password(password, user.password):
        return Token.objects.get(user=user)
    raise Http404("Incorrect credentials")




