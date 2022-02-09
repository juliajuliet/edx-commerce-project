# Generated by Django 3.2.7 on 2022-01-02 10:50

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0011_auto_20220101_1918'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='created',
            field=models.DateTimeField(default=datetime.datetime(2022, 1, 2, 10, 50, 29, 706322, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='listing',
            name='created',
            field=models.DateTimeField(default=datetime.datetime(2022, 1, 2, 10, 50, 29, 705323, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='listing',
            name='image',
            field=models.URLField(blank=True, null=True),
        ),
    ]