# Generated by Django 3.2.7 on 2022-01-02 11:25

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0012_auto_20220102_1750'),
    ]

    operations = [
        migrations.RenameField(
            model_name='listing',
            old_name='image',
            new_name='imageURL',
        ),
        migrations.AddField(
            model_name='listing',
            name='imageFile',
            field=models.ImageField(null=True, upload_to='auctions/static/media'),
        ),
        migrations.AlterField(
            model_name='comment',
            name='created',
            field=models.DateTimeField(default=datetime.datetime(2022, 1, 2, 11, 25, 36, 275743, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='listing',
            name='created',
            field=models.DateTimeField(default=datetime.datetime(2022, 1, 2, 11, 25, 36, 274744, tzinfo=utc)),
        ),
    ]
