from django.http.response import HttpResponse
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.views.generic import TemplateView, CreateView,DetailView
from django.contrib.auth.views import LoginView

from . import forms
from . import models


# Create your views here.


class Homepage(TemplateView):
    template_name = "index.html" 

# class Profile():
def profile(request):
    if request.user.student_id is None:
        return HttpResponse("Please Insert")
    
    return redirect( reverse_lazy("index") )


class UserProfile(DetailView):
    model = models.User
    template_name='account/profile.html'

class Events(TemplateView):
    template_name = "events.html"
    
class Login(TemplateView):
    template_name = "login.html"
    
class Register(CreateView):
    form_class = forms.RegisterForm
    # fields =  ['first_name', 'last_name', 'email', 'username', 'student_id', 'password1','password2']
    success_url = reverse_lazy("index")
    http_method_names = ['get', 'post']
    success_message = "%(username)s was created successfully"
    template_name = "register.html"
    