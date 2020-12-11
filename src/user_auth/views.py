from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView
from django.views.generic.edit import FormView
from django.contrib.auth import login, authenticate
from django.shortcuts import redirect

from user_auth.forms import UserSignUpForm


class UserLoginView(LoginView):
    template_name = 'login.html'


class UserSignUpView(FormView):
    template_name = 'signup.html'
    form_class = UserSignUpForm
    success_url = reverse_lazy('admin:index')

    def form_valid(self, form):
        user = form.save(commit=False)
        # DEBUG: in order to login admin panel
        user.is_staff = True
        user.is_superuser = True
        # ---
        user.save()
        user = authenticate(
            username=form.cleaned_data.get('username'),
            password=form.cleaned_data.get('password1'),
        )
        login(self.request, user)
        return super().form_valid(form)

    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect(reverse_lazy('admin:index'))
        return super().get(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect(reverse_lazy('admin:index'))
        return super().post(request, *args, **kwargs)
