# Generated by Django 4.0.3 on 2022-04-10 11:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("main", "0008_alter_campaign_description"),
    ]

    operations = [
        migrations.AddField(
            model_name="campaign",
            name="picture",
            field=models.CharField(
                choices=[["image/toy.png", "image/toy.png"]], max_length=1000, null=True
            ),
        ),
    ]
