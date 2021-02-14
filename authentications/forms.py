from django import forms
from django.contrib.auth.forms import UserCreationForm

from .models import User


class RegisterForm(forms.ModelForm):
    
    class Meta(UserCreationForm.Meta):
        model = User
        fields = UserCreationForm.Meta.fields + ('student_id',)

    def clean_student_id(self):
        student_id = self.cleaned_data.get('student_id')
        if User.objects.filter(student_id=student_id).exists():
            raise forms.ValidationError("Student Id already exists")
        return student_id

        