from django.contrib import admin
from .models import Vote,Candidate,Election

# Register your models here.
admin.site.register(Candidate)
admin.site.register(Vote)
admin.site.register(Election)
