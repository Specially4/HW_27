# Generated by Django 4.1.1 on 2022-10-15 05:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("selections", "0001_initial"),
    ]

    operations = [
        migrations.RenameField(
            model_name="selection",
            old_name="owmer",
            new_name="owner",
        ),
    ]
