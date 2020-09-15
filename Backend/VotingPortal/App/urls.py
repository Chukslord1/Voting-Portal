from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include
from . import views

app_name = "APP"

urlpatterns = [

    path("", views.index, name="index"),
    path("candidates.html", views.create_vote, name="create_vote"),
    path("results", views.results, name="results"),
    path("login", views.login, name="login"),
    path("register", views.register, name="register")
]
