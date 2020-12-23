from django.urls import path

from user_auth import views

urlpatterns = [
    path('login/', views.UserLoginView.as_view(), name='user-login'),
    path('register/', views.UserSignUpView.as_view(), name='user-register'),
    path('logout/', views.UserLogoutView.as_view(), name='user-logout'),
    path('confirm/', views.EmailConfirmationView.as_view(), name='user-email-confirmation'),
    path('reset_password/', views.PasswordResetView.as_view(), name='password_reset'),
    path('reset_password/done', views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('reset_password/<uidb64>/<token>', views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('reset_password/complete', views.PasswordResetCompleteView.as_view(), name='password_reset_complete')
]
