from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Vote(models.Model):
    title=models.TextField()
    name=models.TextField()
    time=models.DateField(auto_now_add=True)
    user=models.TextField()

    def __str__(self):
        return self.title


class Candidate(models.Model):
    title=models.TextField()
    name=models.TextField()
    vote = models.IntegerField(default='0')
    percent=models.FloatField(default='0')
    image=models.ImageField()

    def __str__(self):
        return self.name

class Election(models.Model):
    name=models.TextField()

class Time(models.Model):
    start=models.DateTimeField()
    end=models.DateTimeField()

class UserProfile(models.Model):
    user = models.OneToOneField(User, related_name="profile", on_delete=models.CASCADE)
    username=models.CharField(max_length=100, null=True,blank=True)
    phone=models.CharField(max_length=100, null=True,blank=True)
