# Generated by Django 4.0.7 on 2022-11-11 15:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('activities', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='activityinstance',
            name='duration',
            field=models.IntegerField(default=0),
        ),
    ]
