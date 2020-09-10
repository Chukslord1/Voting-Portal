from django.db import models

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

    def __str__(self):
        return self.name
