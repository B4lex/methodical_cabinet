from django.urls import path
import django.contrib.auth.views as auth_views

from user_auth import views


urlpatterns = [
    path('login/', views.UserLoginView.as_view(), name='user-login'),
    path('register/', views.UserSignUpView.as_view(), name='user-register'),
    path('logout/', views.UserLogoutView.as_view(), name='user-logout'),
    path('confirm/', views.EmailConfirmationView.as_view(),
         name='user-email-confirmation'),
    path('reset_password/', auth_views.PasswordResetView.as_view(),
         name='user-password-reset'),
    path('reset_password/', auth_views.PasswordResetDoneView.as_view(),
         name='password-reset-confirm'),
    path('reset_password/<uidb64>/<token>', auth_views.PasswordResetConfirmView.as_view(),
         name='user-password-reset'),
    path('reset_password/', auth_views.PasswordResetCompleteView.as_view(),
         name='password-reset-confirm')
]
