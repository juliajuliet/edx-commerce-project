# Generated by Django 3.2.7 on 2022-01-02 11:28

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0013_auto_20220102_1825'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='created',
            field=models.DateTimeField(default=datetime.datetime(2022, 1, 2, 11, 28, 11, 874079, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='listing',
            name='created',
            field=models.DateTimeField(default=datetime.datetime(2022, 1, 2, 11, 28, 11, 873079, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='listing',
            name='imageFile',
            field=models.ImageField(upload_to='auctions/static/media'),
        ),
    ]
