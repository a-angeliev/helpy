
from django.contrib.auth import get_user_model
from django.core.validators import MinLengthValidator, MaxValueValidator, MinValueValidator
from django.db import models


from project.accounts.models import Profile
from project.common.helpers import CityOption, PaymentOptions, PictureOptions

UserModel = get_user_model()


class Shelter(models.Model):
    MAX_TITLE_LENGTH = 70
    MIN_TITLE_LENGTH = 5

    MAX_DESCRIPTION_LENGTH = 255

    MAX_NUMBER_OF_PEOPLE = 100
    MIN_NUMBER_OF_PEOPLE =1

    MAX_ROOM_NUMBER = 100
    MIN_ROOM_NUMBER = 1

    title = models.CharField(
        max_length=MAX_TITLE_LENGTH,
        validators=(MinLengthValidator(MIN_TITLE_LENGTH),),
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
            MaxValueValidator(MAX_NUMBER_OF_PEOPLE),
            MinValueValidator(MIN_NUMBER_OF_PEOPLE),
        )
    )

    room_number = models.IntegerField(validators=(
            MaxValueValidator(MAX_ROOM_NUMBER),
            MinValueValidator(MIN_ROOM_NUMBER),
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
        validators=(MinLengthValidator(MIN_TITLE_LENGTH),),
    )

    created_on = models.DateField(
        auto_now_add=True,
    )

    description = models.TextField(
        max_length=MAX_DESCRIPTION_LENGTH,
    )

    money = models.IntegerField(validators=(MaxValueValidator(10000),))

    compensation = models.CharField(
        max_length=PaymentOptions().max_payment_length(),
        choices=PaymentOptions.PAYMENT,
    )

    city = models.CharField(
        max_length=CityOption().max_city_length(),
        choices=CityOption.CITYS,
    )

    user = models.ForeignKey(Profile, null=True, blank=True, on_delete=models.CASCADE)


class Questionnaire(models.Model):

    TEXT_FIELD_MAX_LENGTH = 512

    created_on = models.DateTimeField(auto_now_add=True)
    food = models.BooleanField()
    blankets = models.BooleanField()
    cloths = models.BooleanField()
    home = models.BooleanField()
    toys = models.BooleanField()
    money = models.BooleanField()
    electric_appliances = models.BooleanField()
    transportation = models.BooleanField()
    phone = models.BooleanField()
    pills = models.BooleanField()
    others = models.BooleanField()
    description = models.TextField(
        max_length=TEXT_FIELD_MAX_LENGTH,
    )

    user = models.ForeignKey(Profile, null=True, blank=True, on_delete=models.CASCADE)


class Campaign(models.Model):

    MAX_TITLE_LENGTH = 70
    MAX_DESCRIPTION_LENGTH = 512
    MAX_WHEN_LENGTH = 70
    MAX_WHERE_LENGTH = 70

    picture = models.CharField(
        max_length=1000,
        choices=PictureOptions.PICTURES,
        null=True,
    )
    created_on = models.DateTimeField(auto_now_add=True)

    title = models.CharField(
        max_length=MAX_TITLE_LENGTH,
    )

    description = models.TextField(
        max_length=MAX_DESCRIPTION_LENGTH,
        null=True,
        blank=True,
    )

    when = models.CharField(
        max_length=MAX_WHEN_LENGTH,
    )

    where = models.CharField(
        max_length=MAX_WHERE_LENGTH,
    )

    user = models.ForeignKey(UserModel, null=True, blank=True, on_delete=models.CASCADE)



