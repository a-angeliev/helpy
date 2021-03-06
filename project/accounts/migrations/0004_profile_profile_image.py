# Generated by Django 4.0.3 on 2022-04-10 16:54

from django.db import migrations, models
import project.common.validators


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_alter_projectuser_email'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='profile_image',
            field=models.ImageField(null=True, upload_to='', validators=[project.common.validators.validate_image]),
        ),
    ]
