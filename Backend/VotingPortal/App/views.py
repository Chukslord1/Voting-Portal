from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Vote,Candidate,Election,Time,UserProfile,Candidate_Reg
from django.http import JsonResponse
from django.contrib.auth.models import User, auth
from django.db.models import Sum
import datetime
from datetime import timezone
# Create your views here.

def index(request):
    honduras="happy hactober"
    return HttpResponse("Hello World")


def login(request):
    if request.method == 'POST':
        phone = request.POST['phone']
        password = request.POST['password']
        if UserProfile.objects.filter(phone=phone):
            username=UserProfile.objects.get(phone=phone).username
        else:
            username=''
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect("candidates.html")
        else:
            context={"message":"Invalid login credentials"}
            return render(request,"login.html",context)
    else:
        return render(request,"login.html")


def register(request):
    if request.method=="POST":
        name= request.POST['name']
        phone=request.POST['phone']
        username = request.POST['username']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']

        if password1 == password2:
            if UserProfile.objects.filter(phone=phone).exists() or User.objects.filter(username=username).exists():
                context={"message":"user already exists"}
                return render(request,"register.html",context)
            else:
                user = User.objects.create(username=username,first_name=name,password=password1, email=email)
                user.set_password(user.password)
                user.save()
                profile=UserProfile.objects.create(user=user,username=username,phone=phone)
                profile.save()
                def_vote=Vote.objects.create(user=username,name="0000",title="0000")
                def_vote.save()
                return redirect("login.html")
        else:
            context={"message":"password dont match"}
            return render(request,"register.html",context)
    else:
        return render(request,"register.html")


def create_vote(request):
    context={"elections":Election.objects.all(),"candidates":Candidate.objects.all(),"times":Time.objects.all(),"voted":Vote.objects.filter(user=request.user)}
    if request.user.is_authenticated:
        if request.method=="POST":
            title=request.POST.get("title")
            name=request.POST.get("name")
            if Candidate.objects.filter(name__icontains=name):
                name=request.POST.get("name")
            else:
                return HttpResponse("NO SUCH CANDIDATE AVAILABLE")
            if Election.objects.filter(name__icontains=title):
                title=request.POST.get("title")
            else:
                return HttpResponse("NO SUCH ELECTION AVAILABLE")
            user=str(request.user)
            if Vote.objects.filter(title=title,user=user).count()<1:
                if datetime.datetime.now(timezone.utc)>Time.objects.get().start and datetime.datetime.now(timezone.utc)<Time.objects.get().end:
                    vote=Vote.objects.create(title=title,name=name,user=user)
                    vote.save()
                    vote_add=Candidate.objects.get(name=name).vote
                    number=int(vote_add)+1
                    vote_new=Candidate.objects.get(name=name)
                    vote_new.vote=number
                    vote_new.save()
                    vote_count=Vote.objects.filter(title=title).count()
                    vote_count_percent=Candidate.objects.all()
                    for i in vote_count_percent:
                        vote_count_percent_save=Candidate.objects.get(name=i.name)
                        number_all=i.vote
                        percent=(number_all/vote_count)*100
                        vote_count_percent_save.percent=percent
                        vote_count_percent_save.save()

                    context={"message":"vote  placed","elections":Election.objects.all(),"candidates":Candidate.objects.all(),"times":Time.objects.all(),"voted":Vote.objects.filter(user=request.user)}
                    return render(request,"candidates.html",context)
                elif datetime.datetime.now(timezone.utc)>Time.objects.get().end:
                    context={"message": "Voting Closed","elections":Election.objects.all(),"candidates":Candidate.objects.all(),"times":Time.objects.all(),"voted":Vote.objects.filter(user=request.user)}
                    return render(request,"candidates.html",context)
                else:
                    print("hello")
                    context={"message":"vote  time not yet","elections":Election.objects.all(),"candidates":Candidate.objects.all(),"times":Time.objects.all(),"voted":Vote.objects.filter(user=request.user)}
                    return render(request,"candidates.html",context)
            elif Vote.objects.filter(title=title,user=user).count()>0:
                context={"message":"You have already voted in this category","elections":Election.objects.all(),"candidates":Candidate.objects.all(),"times":Time.objects.all(),"voted":Vote.objects.filter(user=request.user)}
                return render(request,"candidates.html",context)
            else:
                print("hello worldl")
                return HttpResponse("Error Creating Vote Please Check Arguments")
        else:
            return render(request,"candidates.html",context)
    else:
        return HttpResponse("You are not logged in")


def activity(request):
    context={"results":Candidate.objects.filter(title__icontains="president")}
    return render(request,"activity.html",context)


def results(request):
    context={"results":Candidate.objects.filter(title__icontains="president")}
    return render(request,"results.html",context)
def candidate_reg(request):
    if request.method=="POST":
        title=request.POST.get("title")
        lastname=request.POST.get("lastname")
        othername=request.POST.get("othername")
        address=request.POST.get("address")
        sex=request.POST.get("sex")
        date_of_birth=request.POST.get("dob")
        occupation=request.POST.get("occupation")
        email=request.POST.get("email")
        phone=request.POST.get("phone")
        education=request.POST.get("education")
        chapter=request.POST.get("chapter")
        chapter_year=request.POST.get("chapter_year")
        executive_status=request.POST.get("executive")
        executive_officer=request.POST.get("executive_officer")
        financial=request.POST.get("financial")
        attendance_status=request.POST.get("attendance_status")
        dishonesty_status=request.POST.get("dishonesty")
        position=request.POST.get("position")
        image=request.FILES.get("image")
        candidate_reg=Candidate_Reg.objects.create(title=title,last_name=lastname,other_name=othername,address=address,sex=sex,date_of_birth=date_of_birth,occupation=occupation,email=email,phone=phone,education=education,chapter=chapter,chapter_year=chapter_year,executive_status=executive_status,executive_officer=executive_officer,financial=financial,attendance_status=attendance_status,dishonesty_status=dishonesty_status,position=position,image=image)
        candidate_reg.save()
        context={"message":"Your Registration Is Successful...Please await an Email From Us in A Few Days Time"}
        return render(request,"candidate_reg.html",context)
    else:
        return render(request,"candidate_reg.html")
