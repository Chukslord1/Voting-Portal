# Generated by Django 2.2.4 on 2020-10-05 16:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0018_auto_20201005_1630'),
    ]

    operations = [
        migrations.AddField(
            model_name='candidate_reg',
            name='profile',
            field=models.TextField(blank=True, null=True),
        ),
    ]