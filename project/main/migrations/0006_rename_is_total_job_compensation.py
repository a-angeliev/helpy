# Generated by Django 4.0.3 on 2022-04-07 13:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("main", "0005_alter_job_is_total_alter_job_money"),
    ]

    operations = [
        migrations.RenameField(
            model_name="job",
            old_name="is_total",
            new_name="compensation",
        ),
    ]
