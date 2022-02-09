# Generated by Django 3.2.7 on 2021-12-30 10:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0002_bids_comments_listing'),
    ]

    operations = [
        migrations.CreateModel(
            name='Listings',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=80)),
                ('category', models.CharField(max_length=64)),
                ('image', models.ImageField(height_field=200, upload_to='auctions/static/media', width_field=200)),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('description', models.TextField(max_length=300)),
                ('date', models.DateTimeField()),
            ],
        ),
        migrations.DeleteModel(
            name='Listing',
        ),
    ]