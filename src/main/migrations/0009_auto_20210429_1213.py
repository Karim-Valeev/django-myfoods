# Generated by Django 3.1.7 on 2021-04-29 12:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0008_auto_20210429_1208'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='profile_pic',
            field=models.ImageField(blank=True, default='default_profile_pic.jpg', upload_to=''),
        ),
    ]
