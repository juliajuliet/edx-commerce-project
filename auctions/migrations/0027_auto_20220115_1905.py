# Generated by Django 3.2.7 on 2022-01-15 12:05

import datetime
from django.conf import settings
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0026_auto_20220111_2112'),
    ]

    operations = [
        migrations.AddField(
            model_name='listing',
            name='isActive',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='listing',
            name='watchers',
            field=models.ManyToManyField(blank=True, related_name='watched_listings', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='comment',
            name='created',
            field=models.DateTimeField(default=datetime.datetime(2022, 1, 15, 12, 5, 4, 887820, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='listing',
            name='created',
            field=models.DateTimeField(default=datetime.datetime(2022, 1, 15, 12, 5, 4, 885822, tzinfo=utc)),
        ),
    ]
