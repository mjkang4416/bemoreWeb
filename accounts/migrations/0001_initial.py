# Generated by Django 5.0.2 on 2024-02-07 15:29

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="userList",
            fields=[
                (
                    "id",
                    models.CharField(max_length=25, primary_key=True, serialize=False),
                ),
                ("password", models.CharField(max_length=25, unique=True)),
            ],
        ),
    ]
