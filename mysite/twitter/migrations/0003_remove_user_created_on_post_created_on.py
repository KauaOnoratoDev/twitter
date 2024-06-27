# Generated by Django 5.0.6 on 2024-06-25 10:08

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("twitter", "0002_user_created_on"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="user",
            name="created_on",
        ),
        migrations.AddField(
            model_name="post",
            name="created_on",
            field=models.DateTimeField(
                default=datetime.datetime(
                    2024, 6, 25, 10, 8, 9, 707749, tzinfo=datetime.timezone.utc
                )
            ),
        ),
    ]
