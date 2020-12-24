from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from user_auth.models import Teacher


class UserSignUpForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = Teacher
        fields = ("full_name", "email")


class UserLoginForm(AuthenticationForm):
    def __init__(self, request=None, *args, **kwargs):
        super().__init__(request, *args, **kwargs)
