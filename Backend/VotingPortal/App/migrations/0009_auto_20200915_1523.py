# Generated by Django 2.2.4 on 2020-09-15 14:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0008_auto_20200915_1522'),
    ]

    operations = [
        migrations.AlterField(
            model_name='candidate',
            name='vote',
            field=models.IntegerField(default='0'),
        ),
    ]
