from django.urls import path
from user_auth import views

urlpatterns = [
    path('login/', views.UserLoginView.as_view(), name='user-login'),
    path('register/', views.UserSignUpView.as_view(), name='user-register')
]
