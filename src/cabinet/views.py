from django.views.generic.base import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin


class CabinetMainPageView(LoginRequiredMixin, TemplateView):
    template_name = 'cabinet.html'


class CabinetEditPageView(LoginRequiredMixin, TemplateView):
    template_name = 'cabinet.html'

