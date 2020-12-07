from django.shortcuts import render, HttpResponse, redirect, reverse
from django.http import HttpRequest

# Create your views here.


def login(request):
    if (request.user.is_authenticated):
        return render(request, 'login.html')
    else:
        return redirect(reverse('user-register'))

def register(request):
    return HttpResponse('Registration form.')

