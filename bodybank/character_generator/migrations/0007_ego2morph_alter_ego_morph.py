# Generated by Django 4.1 on 2022-10-05 02:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        (
            "character_generator",
            "0006_remove_morph_mov_base_remove_morph_mov_full_and_more",
        ),
    ]

    operations = [
        migrations.CreateModel(
            name="Ego2Morph",
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
                ("creation_timestamp", models.DateTimeField(auto_now_add=True)),
                (
                    "ego_from",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="related_from_set",
                        to="character_generator.ego",
                    ),
                ),
                (
                    "morph_to",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="related_to_set",
                        to="character_generator.morph",
                    ),
                ),
            ],
        ),
        migrations.AlterField(
            model_name="ego",
            name="morph",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="character_generator.ego2morph",
            ),
        ),
    ]
