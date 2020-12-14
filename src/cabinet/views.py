from django.views.generic.base import TemplateView
from django.views.generic.edit import UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from django.utils.translation import gettext_lazy as _

from user_auth.models import Teacher
from cabinet.forms import CabinetEditForm


class CabinetMainPageView(LoginRequiredMixin, TemplateView):
    template_name = 'cabinet.html'


class CabinetEditPageView(SuccessMessageMixin, LoginRequiredMixin, UpdateView):
    model = Teacher
    form_class = CabinetEditForm
    template_name = 'cabinet_edit.html'
    success_url = reverse_lazy('cabinet-edit')
    success_message = _('Изменения успешно сохранены')

    def get_object(self, queryset=None):
        return self.request.user
