# Generated by Django 3.1 on 2020-08-30 23:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('schools', '0005_auto_20200830_2352'),
    ]

    operations = [
        migrations.AlterField(
            model_name='school',
            name='active',
            field=models.BooleanField(default=True),
        ),
    ]