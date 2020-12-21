from django import forms
from django.contrib.auth.forms import UserCreationForm
from user_auth.models import Teacher


class UserSignUpForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = Teacher
        fields = ("full_name", "email")
