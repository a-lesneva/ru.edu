# Generated by Django 3.1 on 2020-08-30 23:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('schools', '0004_auto_20200830_2351'),
    ]

    operations = [
        migrations.AlterField(
            model_name='school',
            name='details',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='school',
            name='social_media',
            field=models.URLField(blank=True, null=True),
        ),
    ]
