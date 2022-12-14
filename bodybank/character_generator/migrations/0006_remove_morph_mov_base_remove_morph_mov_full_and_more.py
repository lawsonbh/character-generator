# Generated by Django 4.1 on 2022-09-29 12:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("character_generator", "0005_movement"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="morph",
            name="mov_base",
        ),
        migrations.RemoveField(
            model_name="morph",
            name="mov_full",
        ),
        migrations.RemoveField(
            model_name="morph",
            name="movtype",
        ),
        migrations.AddField(
            model_name="morph",
            name="movtype",
            field=models.ManyToManyField(
                related_name="movement_systems", to="character_generator.movement"
            ),
        ),
    ]
