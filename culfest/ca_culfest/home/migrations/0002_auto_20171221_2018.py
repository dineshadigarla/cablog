# Generated by Django 2.0 on 2017-12-21 20:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='photo_url',
            field=models.URLField(blank=True, default='http://graph.facebook.com/<django.db.models.query_utils.DeferredAttribute object at 0x7ff012622f60>/picture', max_length=400),
        ),
    ]
