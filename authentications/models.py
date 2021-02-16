from django.db import models 
from django.contrib.auth.models import AbstractUser 
from django.utils.translation import gettext_lazy as _


import uuid 

class Role(models.Model):
    
    choice = (
        ("PRESIDENT","President"),
        ("V_PRESIDENT","V President"),
        ("HEAD", "Head"), 
        ("SPECIAL_COMMITTEE", "Special Committee"),
        ("MEMBER", "Member")
    )
    role = models.CharField(max_length=20, choices=choice)
    
    def __str__(self):
        return f"{ self.role }"
    
def user_directory_path(instance, filename):
    ext = (filename).split(".")[-1]
    filename = str(uuid.uuid1())
    return f'users/{ instance.user.id + filename}.{ext}'    

class User(AbstractUser):
    
    DIVISION = (
        ("cpd", "Competitive Programming"),
        ("development", "Development"),
        ("capacity","Capacity Building")
    )
    
    student_id = models.CharField(max_length=20, blank=True, null=True)
    role = models.ForeignKey(Role, verbose_name=_("Role"), default=5, on_delete=models.CASCADE, blank=True, null=True)
    division = models.CharField(max_length=20, choices=DIVISION, blank=True, null=True)
    profile = models.ImageField(_("Image"), upload_to=user_directory_path,default="user/null.png", blank=True, null=True)
    
    def __str__(self) -> str:
        return f"{self.username}"
    

