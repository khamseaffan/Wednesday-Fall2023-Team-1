# Generated by Django 4.2.6 on 2023-11-28 02:43

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Track",
            fields=[
                (
                    "track_id",
                    models.CharField(max_length=250, primary_key=True, serialize=False),
                ),
                ("track_lyrics_vibe", models.CharField(max_length=250, null=True)),
                ("track_audio_vibe", models.CharField(max_length=250, null=True)),
                ("upvote_count", models.IntegerField(default=0)),
                ("downvote_count", models.IntegerField(default=0)),
            ],
        ),
    ]
