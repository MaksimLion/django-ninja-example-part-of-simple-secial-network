from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.db import models
from .managers import UserManager
from .utils import get_user_photo_path
from .validators import UsernameValidator, validate_birthday


class User(AbstractBaseUser, PermissionsMixin):
    username_validators = UsernameValidator()

    username = models.CharField(
        db_index=True,
        max_length=50,
        unique=True,
        validators=[username_validators],
        error_messages={"unique": "A user with that username already exists"}
    )
    photo = models.ImageField(
        upload_to=get_user_photo_path, null=True, blank=True
    )
    email = models.EmailField(db_index=True, unique=True)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    birthday = models.DateField(validators=[validate_birthday])

    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    objects = UserManager()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["username", "first_name", "last_name", "birthday",]

    def __str__(self):
        return self.username

    def get_full_name(self):
        return self.first_name + " " + self.last_name


