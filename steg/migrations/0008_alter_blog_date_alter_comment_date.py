# Generated by Django 4.2.2 on 2023-06-22 06:24

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('steg', '0007_auto_20230621_1256'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='date',
            field=models.DateField(default=datetime.datetime(2023, 6, 22, 6, 24, 35, 848844, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='comment',
            name='date',
            field=models.DateField(default=datetime.datetime(2023, 6, 22, 6, 24, 35, 849267, tzinfo=datetime.timezone.utc)),
        ),
    ]