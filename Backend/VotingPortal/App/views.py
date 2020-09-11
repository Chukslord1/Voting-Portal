from django.shortcuts import render
from django.http import HttpResponse
from .models import Vote,Candidate,Election
from django.http import JsonResponse
from django.contrib.auth.models import User, auth
# Create your views here.

def index(request):
    return HttpResponse("Hello World")


def login(request):
    if request.method == 'GET':
        username = request.GET['username']
        password = request.GET['password']
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return HttpResponse("you are Logged In ")
        else:
            return HttpResponse("Invalid Credentials")
    else:
        return HttpResponse("not valid request method")

def register(request):
    if request.method=="GET":
        username = request.GET['username']
        email = request.GET['email']
        password1 = request.GET['password1']
        password2 = request.GET['password2']

        if password1 == password2:
            if User.objects.filter(email=email).exists() or User.objects.filter(username=username).exists():
                return HttpResponse("user already exists")
            else:
                user = User.objects.create(username=username, password=password1, email=email)
                user.set_password(user.password)
                user.save()
                return HttpResponse("registered successfully")
        else:
            return HttpResponse("confirm password does not match")
    else:
        return HttpResponse("not valid request method")


def create_vote(request):
    if request.user.is_authenticated:
        title=request.GET.get("title")
        name=request.GET.get("name")
        if Candidate.objects.filter(name__icontains=name):
            name=request.GET.get("name")
        else:
            return HttpResponse("NO SUCH CANDIDATE AVAILABLE")
        if Election.objects.filter(name__icontains=title):
            title=request.GET.get("title")
        else:
            return HttpResponse("NO SUCH ELECTION AVAILABLE")
        user=str(request.user)
        if Vote.objects.filter(title=title,user=user).count()<1:
            vote=Vote.objects.create(title=title,name=name,user=user)
            vote.save()
            vote_add=Candidate.objects.get(name=name).vote
            number=int(vote_add)+1
            vote_new=Candidate.objects.get(name=name)
            vote_new.vote=number
            vote_new.save()
            return HttpResponse("Done")
        elif Vote.objects.filter(title=title,user=user).count()>0:
            return HttpResponse("You have already voted in this category")
        else:
            return HttpResponse("Error Creating Vote Please Check Arguments")
    else:
        return HttpResponse("You are not logged in")



def results(request):
    title=request.GET.get("title")
    candidates=[]
    results=Vote.objects.all().count()
    if title:
        for i in Candidate.objects.filter(title=title):
            candidates.append({"candidate":i.name,"votes":i.vote})
        return JsonResponse({"success":True,"results":candidates,"total_votes":results,"election_name":title})
    else:
        return HttpResponse("Error Viewing Results Please Check Arguments")
