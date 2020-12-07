from django.urls import path
from user_auth import views

urlpatterns = [
    path('login/', views.login, name='user-login'),
    path('register/', views.register, name='user-register')
]