

from django.contrib.auth import get_user_model
from django.core.validators import MinLengthValidator, MaxValueValidator
from django.db import models

# Create your models here.
from django.http import request

from project.accounts.models import Profile
from project.common.helpers import CityOption, PaymentOptions

UserModel = get_user_model()


class Shelter(models.Model):
    MAX_TITLE_LENGTH = 70
    MIN_TITLE_LENGTH = 5

    MAX_DESCRIPTION_LENGTH = 255

    title = models.CharField(
        max_length= MAX_TITLE_LENGTH,
        validators=(
            MinLengthValidator(MIN_TITLE_LENGTH),
        ),
    )

    created_on = models.DateTimeField(
        auto_now_add=True,
    )

    city = models.CharField(
        max_length=CityOption().max_city_length(),
        choices=CityOption.CITYS,
    )

    description = models.TextField(
        max_length=MAX_DESCRIPTION_LENGTH,
    )

    ppl_number = models.IntegerField(
        validators=(
            MaxValueValidator(100),
        )
    )

    room_number = models.IntegerField(
        validators=(
            MaxValueValidator(100),
        )
    )

    has_wc = models.BooleanField(
        default=False,
    )
    has_net = models.BooleanField(
        default=False,
    )
    has_kitchen = models.BooleanField(
        default=False,
    )
    has_tv = models.BooleanField(
        default=False,
    )
    has_garage = models.BooleanField(
        default=False,
    )

    user = models.ForeignKey(Profile, null=True, blank=True, on_delete=models.CASCADE)


class Job(models.Model):

    MAX_TITLE_LENGTH = 70
    MIN_TITLE_LENGTH = 5

    MAX_DESCRIPTION_LENGTH = 255

    title = models.CharField(
        max_length=MAX_TITLE_LENGTH,
        validators=(
            MinLengthValidator(MIN_TITLE_LENGTH),
        ),
    )

    created_on = models.DateField(
        auto_now_add=True,
    )

    description = models.TextField(
        max_length=MAX_DESCRIPTION_LENGTH,
    )

    money = models.IntegerField(
        validators=(
            MaxValueValidator(100),
        )
    )

    compensation = models.CharField(
        max_length=PaymentOptions().max_payment_length(),
        choices=PaymentOptions.PAYMENT,
    )

    city = models.CharField(
        max_length=CityOption().max_city_length(),
        choices=CityOption.CITYS,
    )

    user = models.ForeignKey(Profile, null=True, blank=True, on_delete=models.CASCADE)
