import datetime

from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.core.validators import MaxValueValidator, MinLengthValidator, EmailValidator
from django.db import models
from django.contrib.auth import models as auth_models
from cloudinary import models as cloudinary_models
from project.accounts.managers import ProjectUserManager
from project.common.validators import validate_image


class ProjectUser(auth_models.AbstractBaseUser, auth_models.PermissionsMixin):

    email = models.EmailField(
        unique=True,
        validators=(EmailValidator,)
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

    USERNAME_FIELD = "email"

    objects = ProjectUserManager()


class Profile(models.Model):

    FIRST_NAME_MAX_LENGTH = 30
    LAST_NAME_MAX_LENGTH = 30
    ABOUT_YOURSELF_MAX_LENGTH = 512

    MALE = "Male"
    FEMALE = "Female"

    GENDERS = [
        (x, x)
        for x in (
            MALE,
            FEMALE,
        )
    ]

    first_name = models.CharField(max_length=FIRST_NAME_MAX_LENGTH,)

    last_name = models.CharField(max_length=LAST_NAME_MAX_LENGTH, )

    # picture = models.URLField()

    profile_image = cloudinary_models.CloudinaryField('image')

    phone_number = models.IntegerField(
        validators=(
            MaxValueValidator(15),
            MinLengthValidator(5),)
    )

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

    def save(self, *args, **kwargs):
        if self.date_of_birth > datetime.date.today():
            raise ValidationError("The date cannot be in the past!")
        super(Profile, self).save(*args, **kwargs)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
