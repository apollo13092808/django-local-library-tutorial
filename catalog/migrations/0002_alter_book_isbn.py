# Generated by Django 4.2.5 on 2023-09-17 09:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("catalog", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="book",
            name="isbn",
            field=models.CharField(
                help_text='13 Character <a href="https://www.isbn-international.org/content/isbn-standard">ISBN number</a>',
                max_length=15,
                unique=True,
                verbose_name="ISBN",
            ),
        ),
    ]
