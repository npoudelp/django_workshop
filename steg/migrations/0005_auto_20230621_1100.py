# Generated by Django 3.2.19 on 2023-06-21 05:15

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('steg', '0004_auto_20230620_1830'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='image',
            field=models.ImageField(default=(), upload_to='blog_photo'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='blog',
            name='date',
            field=models.DateField(default=datetime.datetime(2023, 6, 21, 5, 14, 32, 485597, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='comment',
            name='date',
            field=models.DateField(default=datetime.datetime(2023, 6, 21, 5, 14, 32, 485994, tzinfo=utc)),
        ),
    ]