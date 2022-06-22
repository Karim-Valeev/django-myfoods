# Generated by Django 3.1.7 on 2021-04-26 13:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("main", "0005_auto_20210426_1256"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="item",
            name="comments",
        ),
        migrations.AlterField(
            model_name="itemcomment",
            name="item",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, related_name="comments", to="main.item"
            ),
        ),
    ]
