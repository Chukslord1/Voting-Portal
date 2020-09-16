from django.contrib import admin
from .models import Vote,Candidate,Election,Time,UserProfile

# Register your models here.
admin.site.register(Candidate)
admin.site.register(Vote)
admin.site.register(Election)
admin.site.register(Time)
admin.site.register(UserProfile)
