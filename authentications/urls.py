from django.urls import path, include

from . import views 

urlpatterns = [
    path("", views.Homepage.as_view(), name="index"),
    path("contest", views.Contest.as_view(), name="contest"),
    path("login", views.Login.as_view(), name="login"),
    path("profile", views.profile, name="profile"),
    path("register", views.Register.as_view(), name="register"),
]
