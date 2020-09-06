from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include
from . import views

app_name = "APP"

urlpatterns = [

    path("", views.index, name="index"),
    path("create_vote", views.create_vote, name="create_vote"),
    path("count_vote", views.count_vote, name="count_vote"),
    path("results", views.results, name="results")
]
