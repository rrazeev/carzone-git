# Generated by Django 3.0.7 on 2021-03-07 03:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contacts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='car_id',
            field=models.IntegerField(),
        ),
    ]
