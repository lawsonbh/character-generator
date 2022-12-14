# Generated by Django 4.1 on 2022-10-07 02:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("character_generator", "0010_career_career2skills"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="item",
            name="description",
        ),
        migrations.AddField(
            model_name="item",
            name="desc",
            field=models.TextField(default="", verbose_name="Description"),
        ),
        migrations.AddField(
            model_name="item",
            name="itype",
            field=models.CharField(
                choices=[
                    ("Common Tech & Ware", "Common Tech & Ware"),
                    ("Mission Gear", "Mission Gear"),
                ],
                default="Common Tech & Ware",
                max_length=30,
                verbose_name="Item Type",
            ),
        ),
    ]
