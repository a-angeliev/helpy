from django.contrib.auth.models import User
from django.db import models
from django.contrib.auth import models as auth_models
# Create your models here.
from project.accounts.managers import ProjectUserManager


class ProjectUser(auth_models.AbstractBaseUser, auth_models.PermissionsMixin):

    email = models.EmailField(
        unique=True,
    )

    date_joined = models.DateTimeField(
        auto_now_add=True,
    )

    is_staff = models.BooleanField(
        default=False,
    )

    is_helper = models.BooleanField(
        default=False,
    )

    is_refugee = models.BooleanField(
        default=False,
    )

    USERNAME_FIELD = 'email'

    objects = ProjectUserManager()


class Profile(models.Model):

    FIRST_NAME_MAX_LENGTH = 30
    LAST_NAME_MAX_LENGTH = 30
    ABOUT_YOURSELF_MAX_LENGTH = 512

    MALE = 'Male'
    FEMALE = 'Female'

    GENDERS = [(x, x) for x in (MALE, FEMALE, )]

    first_name = models.CharField(
        max_length=FIRST_NAME_MAX_LENGTH,
        validators=(

        )
    )

    last_name = models.CharField(
        max_length=LAST_NAME_MAX_LENGTH,
        validators=(

        )
    )

    picture = models.URLField()

    phone_number = models.IntegerField()

    date_of_birth = models.DateField(
        null=True,
        blank=True,
    )

    gender = models.CharField(
        max_length=max(len(x) for x, _ in GENDERS),
        choices=GENDERS,
    )

    about_yourself = models.TextField(
        max_length=ABOUT_YOURSELF_MAX_LENGTH,
    )

    user = models.OneToOneField(
        ProjectUser,
        on_delete=models.CASCADE,
        primary_key=True,
    )

    def __str__(self):
        return f'{self.first_name} {self.last_name}'
