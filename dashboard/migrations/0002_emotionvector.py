# Generated by Django 4.2.6 on 2023-11-06 23:01

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("dashboard", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="EmotionVector",
            fields=[
                (
                    "emotion",
                    models.CharField(max_length=250, primary_key=True, serialize=False),
                ),
                ("vector", models.TextField()),
            ],
        ),
    ]