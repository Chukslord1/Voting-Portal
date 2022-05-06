from django.contrib import admin
from .models import Vote,Candidate,Election,Time,UserProfile,Candidate_Reg

# specify readonly details in admin

class TableAdmin(admin.ModelAdmin):
    readonly_fields=('title','name','name_title','position','dishonesty_status','executive_status','attendance_status','financial','executive_officer','chapter_year','chapter','education','graduation_date','admission_date','phone','email','occupation','date_of_birth','sex','address','other_name','profile','percent','image','vote')

class UserAdmin(admin.ModelAdmin):
    readonly_fields=('user','username','phone','address','sex','date_of_birth','admission_year','graduation_year','thsosa_chapter','registration_year','attendance_status','dishonesty_status','image')
# Register your models here.

# registering models to admin
admin.site.register(Candidate,TableAdmin)
admin.site.register(Election)
admin.site.register(Time)
admin.site.register(UserProfile,UserAdmin)
