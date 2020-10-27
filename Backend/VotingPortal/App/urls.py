from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include
from . import views

app_name = "APP"

urlpatterns = [

    path("", views.index, name="index"),
    path("index.html", views.index, name="index"),
    path("candidates.html", views.create_vote, name="create_vote"),
    path("results.html", views.results, name="results"),
    path("activity.html", views.activity, name="activity"),
    path("login.html", views.login, name="login"),
    path("register.html", views.register, name="register"),
    path("candidate_reg", views.candidate_reg, name="candidate_reg"),
    path("voters-approved", views.voters_approved, name="voters_approved")
]
