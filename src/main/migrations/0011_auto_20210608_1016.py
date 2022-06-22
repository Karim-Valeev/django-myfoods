# Generated by Django 3.1.7 on 2021-06-08 10:16

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("main", "0010_auto_20210429_1233"),
    ]

    operations = [
        migrations.AddField(
            model_name="item",
            name="like_counter",
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name="user",
            name="likes",
            field=models.ManyToManyField(related_name="likes", through="main.ItemLike", to="main.Item"),
        ),
        migrations.AlterField(
            model_name="basket",
            name="created_at",
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AlterField(
            model_name="basket",
            name="delivery_address",
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name="itemlike",
            name="item",
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to="main.item"),
        ),
        migrations.AlterField(
            model_name="itemlike",
            name="owner",
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
