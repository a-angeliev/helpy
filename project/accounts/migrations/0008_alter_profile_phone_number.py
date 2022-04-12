# Generated by Django 4.0.3 on 2022-04-12 17:26

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0007_alter_profile_phone_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='phone_number',
            field=models.IntegerField(validators=[django.core.validators.MaxValueValidator(99999999999999)]),
        ),
    ]
