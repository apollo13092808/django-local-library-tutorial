# Generated by Django 4.2.5 on 2023-09-20 02:47

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("catalog", "0005_alter_bookinstance_date_published"),
    ]

    operations = [
        migrations.AlterField(
            model_name="bookinstance",
            name="date_published",
            field=models.DateField(
                blank=True,
                default=datetime.datetime(
                    2023, 9, 20, 2, 47, 52, 100036, tzinfo=datetime.timezone.utc
                ),
                null=True,
            ),
        ),
        migrations.AlterField(
            model_name="bookinstance",
            name="due_back",
            field=models.DateField(
                blank=True,
                default=datetime.datetime(
                    2023, 9, 20, 2, 47, 52, 100059, tzinfo=datetime.timezone.utc
                ),
                null=True,
            ),
        ),
    ]
