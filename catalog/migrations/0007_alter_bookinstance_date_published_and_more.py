# Generated by Django 4.2.5 on 2023-09-20 02:49

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("catalog", "0006_alter_bookinstance_date_published_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="bookinstance",
            name="date_published",
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name="bookinstance",
            name="due_back",
            field=models.DateField(
                blank=True, default=datetime.date(2023, 9, 20), null=True
            ),
        ),
    ]
