import hashlib

from django.utils import timezone
import django.contrib.auth.views as auth_views
from django.views.generic.edit import FormView
from django.views.generic import TemplateView
from django.contrib.auth import login, authenticate
from django.shortcuts import redirect
from django.conf import settings
from django.core.mail import send_mail
from django.utils.translation import gettext_lazy as _

from user_auth.forms import UserSignUpForm


class UserLoginView(auth_views.LoginView):
    template_name = 'login.html'
    redirect_authenticated_user = True


class UserSignUpView(FormView):
    template_name = 'signup.html'
    form_class = UserSignUpForm
    success_url = settings.LOGIN_REDIRECT_URL

    def form_valid(self, form):
        user = form.save(commit=False)
        # DEBUG: in order to login admin panel
        user.is_staff = True
        user.is_superuser = True
        # ---
        user.save()
        user = authenticate(
            email=form.cleaned_data.get('email'),
            password=form.cleaned_data.get('password1'),
        )
        login(self.request, user)
        return super().form_valid(form)

    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect(self.success_url)
        return super().get(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect(self.success_url)
        return super().post(request, *args, **kwargs)


class UserLogoutView(auth_views.LogoutView):
    next_page = '/'


class EmailConfirmationView(TemplateView):
    template_name = 'email_confirmation_info.html'

    def get(self, request, *args, **kwargs):
        user = request.user
        if not user.email_verification:
            token = request.GET.get('token')
            if token and token_is_valid(request.user, token):
                user.email_verification = timezone.now()
                user.save()
                return redirect(UserSignUpView.success_url)
            else:
                message = f'http://127.0.0.1:8000/confirm?token={generate_token(user)}'
                send_mail(_('Методический кабинет'), message, settings.EMAIL_HOST_USER, [user.email])
                return super().get(request, *args, **kwargs)
        else:
            return redirect(settings.LOGIN_REDIRECT_URL)


def generate_token(user):
    return hashlib.sha256(
        user.date_joined.strftime('%Y%m%d%H%M%S%f').encode('utf-8')
    ).hexdigest()


def token_is_valid(user, token):
    return generate_token(user) == token


class EmailConfirmationRequiredMixin:
    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated and not request.user.email_verification:
            return redirect('user-email-confirmation')
        return super().dispatch(request, *args, **kwargs)


class HandleArbitraryPasswordResetMixin:
    def dispatch(self, request, *args, **kwargs):
        print(request.META.get('HTTP_REFERER'))
        if request.META.get('HTTP_REFERER') and not request.user.is_authenticated:
            return super().dispatch(request, *args, **kwargs)
        return redirect('password_reset')


class PasswordResetView(auth_views.PasswordResetView):
    template_name = 'password_reset/password_reset.html'


class PasswordResetDoneView(HandleArbitraryPasswordResetMixin,
                            auth_views.PasswordResetDoneView):
    template_name = 'password_reset/password_reset_done.html'


class PasswordResetConfirmView(auth_views.PasswordResetConfirmView):
    template_name = 'password_reset/password_reset_confirm.html'


class PasswordResetCompleteView(HandleArbitraryPasswordResetMixin,
                                auth_views.PasswordResetCompleteView):
    template_name = 'password_reset/password_reset_complete.html'
