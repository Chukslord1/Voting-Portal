from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include
from . import views

app_name = "APP"

urlpatterns = [

    path("", views.login, name="login"),
    path("candidates.html", views.create_vote, name="create_vote"),
    path("results.html", views.results, name="results"),
    path("login.html", views.login, name="login"),
    path("register.html", views.register, name="register")
]
