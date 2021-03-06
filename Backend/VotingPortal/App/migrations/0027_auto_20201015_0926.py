# Generated by Django 2.2.4 on 2020-10-15 08:26

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0026_auto_20201015_0925'),
    ]

    operations = [
        migrations.AlterField(
            model_name='candidate',
            name='address',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='candidate',
            name='admission_date',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='candidate',
            name='approved',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='candidate',
            name='attendance_status',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='candidate',
            name='chapter',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='candidate',
            name='chapter_year',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='candidate',
            name='date_of_birth',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='candidate',
            name='dishonesty_status',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='candidate',
            name='education',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='candidate',
            name='email',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='candidate',
            name='executive_officer',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='candidate',
            name='executive_status',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='candidate',
            name='financial',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='candidate',
            name='graduation_date',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='candidate',
            name='image',
            field=models.ImageField(upload_to=''),
        ),
        migrations.AlterField(
            model_name='candidate',
            name='name',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='candidate',
            name='name_title',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='candidate',
            name='occupation',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='candidate',
            name='other_name',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='candidate',
            name='percent',
            field=models.FloatField(default='0'),
        ),
        migrations.AlterField(
            model_name='candidate',
            name='phone',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='candidate',
            name='position',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='candidate',
            name='profile',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='candidate',
            name='sex',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='candidate',
            name='title',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='candidate',
            name='vote',
            field=models.IntegerField(default='0'),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='address',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='admission_year',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='attendance_status',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='date_of_birth',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='dishonesty_status',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='graduation_year',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='phone',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='registration_year',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='sex',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='thsosa_chapter',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='profile', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='username',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
