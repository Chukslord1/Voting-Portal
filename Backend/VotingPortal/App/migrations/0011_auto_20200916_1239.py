# Generated by Django 2.2.4 on 2020-09-16 11:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0010_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='time',
            name='end',
            field=models.DateTimeField(),
        ),
        migrations.AlterField(
            model_name='time',
            name='start',
            field=models.DateTimeField(),
        ),
    ]
