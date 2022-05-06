from django.db import models
from django.contrib.auth.models import User

# Create your models here.

# vote model
class Vote(models.Model):
    title=models.TextField()
    name=models.TextField()
    time=models.DateField(auto_now_add=True)
    user=models.CharField(max_length=100)

    def __str__(self):
        return self.title

# candidate model for election
class Candidate(models.Model):
    title=models.TextField(null=True,blank=True)
    name_title=models.TextField(null=True,blank=True)
    name=models.TextField(null=True,blank=True)
    vote = models.IntegerField(default='0')
    percent=models.FloatField(default='0')
    image=models.ImageField()
    profile=models.TextField(null=True,blank=True)
    other_name=models.TextField(null=True,blank=True)
    address=models.TextField(null=True,blank=True)
    sex=models.TextField(null=True,blank=True)
    date_of_birth=models.TextField(null=True,blank=True)
    occupation=models.TextField(null=True,blank=True)
    email=models.TextField(null=True,blank=True)
    phone=models.TextField(null=True,blank=True)
    admission_date=models.TextField(null=True,blank=True)
    graduation_date=models.TextField(null=True,blank=True)
    education=models.TextField(null=True,blank=True)
    chapter=models.TextField(null=True,blank=True)
    chapter_year=models.TextField(null=True,blank=True)
    executive_status=models.TextField(null=True,blank=True)
    executive_officer=models.TextField(null=True,blank=True)
    financial=models.TextField(null=True,blank=True)
    attendance_status=models.TextField(null=True,blank=True)
    dishonesty_status=models.TextField(null=True,blank=True)
    position=models.TextField(null=True,blank=True)
    approved=models.BooleanField(default=False)

    def __str__(self):
        return self.name

class Election(models.Model):
    name=models.TextField()
    def __str__(self):
        return self.name

# time schedule model
class Time(models.Model):
    name=models.TextField(null=True,blank=True)
    start=models.DateTimeField()
    end=models.DateTimeField()
    def __str__(self):
        return self.name

# models for voters profiles
class UserProfile(models.Model):
    user = models.OneToOneField(User, related_name="profile", on_delete=models.CASCADE)
    username=models.CharField(max_length=100, null=True,blank=True)
    phone=models.CharField(max_length=100, null=True,blank=True)
    address=models.CharField(max_length=100, null=True,blank=True)
    sex=models.CharField(max_length=100, null=True,blank=True)
    date_of_birth=models.CharField(max_length=100, null=True,blank=True)
    admission_year=models.CharField(max_length=100, null=True,blank=True)
    graduation_year=models.CharField(max_length=100, null=True,blank=True)
    thsosa_chapter=models.CharField(max_length=100, null=True,blank=True)
    registration_year=models.CharField(max_length=100, null=True,blank=True)
    attendance_status=models.TextField(null=True,blank=True)
    dishonesty_status=models.TextField(null=True,blank=True)
    image=models.ImageField(null=True,blank=True)
    approved=models.BooleanField(default=False)

    def __str__(self):
        return self.username

# model for candidate registration
class Candidate_Reg(models.Model):
    title=models.TextField(null=True,blank=True)
    profile=models.TextField(null=True,blank=True)
    vote = models.IntegerField(default='0')
    percent=models.FloatField(default='0')
    last_name=models.TextField(null=True,blank=True)
    other_name=models.TextField(null=True,blank=True)
    address=models.TextField(null=True,blank=True)
    sex=models.TextField(null=True,blank=True)
    date_of_birth=models.TextField(null=True,blank=True)
    occupation=models.TextField(null=True,blank=True)
    email=models.TextField(null=True,blank=True)
    phone=models.TextField(null=True,blank=True)
    admission_date=models.TextField(null=True,blank=True)
    graduation_date=models.TextField(null=True,blank=True)
    education=models.TextField(null=True,blank=True)
    chapter=models.TextField(null=True,blank=True)
    chapter_year=models.TextField(null=True,blank=True)
    executive_status=models.TextField(null=True,blank=True)
    executive_officer=models.TextField(null=True,blank=True)
    financial=models.TextField(null=True,blank=True)
    attendance_status=models.TextField(null=True,blank=True)
    dishonesty_status=models.TextField(null=True,blank=True)
    position=models.TextField(null=True,blank=True)
    image=models.ImageField(null=True,blank=True)
    approved=models.BooleanField(default=False)

    def __str__(self):
        return self.last_name
