from django.urls import path, include

from . import views 

urlpatterns = [
    path("", views.Homepage.as_view(), name="index"),
    path("contest", views.Contest.as_view(), name="contest"),
]
