# Generated by Django 2.2.4 on 2020-10-05 10:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0014_auto_20200930_2221'),
    ]

    operations = [
        migrations.CreateModel(
            name='Candidate_Reg',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.TextField()),
                ('last_name', models.TextField()),
                ('other_name', models.TextField()),
                ('address', models.TextField()),
                ('sex', models.TextField()),
                ('date_of_birth', models.TextField()),
                ('occupation', models.TextField()),
                ('email', models.TextField()),
                ('phone', models.TextField()),
                ('education', models.TextField()),
                ('chapter', models.TextField()),
                ('chapter_year', models.TextField()),
                ('executive_status', models.TextField()),
                ('financial_status', models.TextField()),
                ('attendance_status', models.TextField()),
                ('dishonesty_status', models.TextField()),
                ('position', models.TextField()),
                ('image', models.ImageField(upload_to='')),
            ],
        ),
    ]
