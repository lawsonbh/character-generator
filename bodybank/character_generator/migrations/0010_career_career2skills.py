# Generated by Django 4.1 on 2022-10-07 02:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("character_generator", "0009_background_skill_alter_morph_mtype_and_more"),
    ]

    operations = [
        migrations.CreateModel(
            name="Career",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=100)),
                ("desc", models.TextField(default="", verbose_name="Description")),
            ],
        ),
        migrations.CreateModel(
            name="Career2Skills",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("modifier", models.PositiveIntegerField(default=0)),
                (
                    "career",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="career_to_skill",
                        to="character_generator.career",
                    ),
                ),
                (
                    "skills",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="skill_to_career",
                        to="character_generator.skill",
                    ),
                ),
            ],
        ),
    ]