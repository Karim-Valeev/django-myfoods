# Generated by Django 3.1.7 on 2021-04-29 12:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("main", "0009_auto_20210429_1213"),
    ]

    operations = [
        migrations.AlterField(
            model_name="user",
            name="profile_pic",
            field=models.ImageField(default="default_profile_pic.jpg", upload_to=""),
        ),
    ]
