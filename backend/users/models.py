from django.contrib.auth.models import AbstractBaseUser
from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

from users.managers import UserManager


class UserRoles(models.TextChoices):
    USER = 'user'
    ADMIN = 'admin'


class User(AbstractBaseUser):
    email = models.EmailField(unique=True)
    role = models.CharField(max_length=5, choices=UserRoles.choices, default=UserRoles.USER)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    phone = PhoneNumberField()
    is_active = models.BooleanField(default=True)
    image = models.ImageField(upload_to='user/', default='user/default_user.png')

    objects = UserManager()

    USERNAME_FIELD = 'email'

    REQUIRED_FIELDS = ['first_name', 'last_name', 'phone', 'role']

    @property
    def is_user(self):
        return self.role == UserRoles.USER

    @property
    def is_admin(self):
        return self.role == UserRoles.ADMIN

    @property
    def is_superuser(self):
        return self.role == UserRoles.ADMIN

    @property
    def is_staff(self):
        return self.role == UserRoles.ADMIN

    def has_perm(self, perm, obj=None):
        return self.role == UserRoles.ADMIN

    def has_module_perms(self, app_label):
        return self.role == UserRoles.ADMIN