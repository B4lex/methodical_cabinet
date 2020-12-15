from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from user_auth import views


urlpatterns = [
    path('login/', views.UserLoginView.as_view(), name='user-login'),
    path('register/', views.UserSignUpView.as_view(), name='user-register'),
    path('logout/', views.UserLogoutView.as_view(), name='user-logout')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
