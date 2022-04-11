# Generated by Django 4.0.3 on 2022-04-10 15:04

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_alter_profile_phone_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='projectuser',
            name='email',
            field=models.EmailField(max_length=254, unique=True, validators=[django.core.validators.EmailValidator]),
        ),
    ]