from django.shortcuts import render
from django.http import HttpResponse
from .models import Vote,Candidate
from django.http import JsonResponse
# Create your views here.

def index(request):
    return HttpResponse("Hello World")


def create_vote(request):
    title=request.GET.get("title")
    name=request.GET.get("name")
    time=request.GET.get("time")
    user=request.GET.get("user")
    if title:
        vote=Vote.objects.create(title=title,name=name,time=time,user=user)
        vote.save()
        return HttpResponse("Done")
    else:
        return HttpResponse("Error Creating Vote Please Check Arguments")

def count_vote(request):
    title=request.GET.get("title")
    name=request.GET.get("name")
    if title and name:
        vote_count=Vote.objects.filter(title=title,name=name).count()
        count=str(vote_count)
        results="for the title of "+title+" candidate "+name+" has "+count+" votes"
        return HttpResponse(results)
    else:
        return HttpResponse("Error Vote Please Check Arguments")

def results(request):
    title=request.GET.get("title")
    result_candidate=[]
    candidates=[]
    results=Vote.objects.all().count()
    if title:
        for i in Candidate.objects.filter(title=title):
            result_candidate.append((Vote.objects.filter(name=i.name)))
            candidates.append({"candidate":i.name})
        return JsonResponse({"success":True,"message":{"candidate":candidates,"result":result_candidate},"total_votes":results})
    else:
        return HttpResponse("Error Viewing Results Please Check Arguments")
