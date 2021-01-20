from django.views.generic.base import TemplateView
from django.views.generic.edit import UpdateView, CreateView
from django.views.generic.list import ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from django.utils.translation import gettext_lazy as _

from user_auth.models import Teacher
from user_auth.views import EmailConfirmationRequiredMixin
from cabinet.forms import CabinetEditForm
from cabinet.models import TeachingMaterial, ScientificMaterial


class CabinetMainPageView(EmailConfirmationRequiredMixin,
                          LoginRequiredMixin, TemplateView):
    template_name = 'cabinet_index.html'


class CabinetEditPageView(EmailConfirmationRequiredMixin, SuccessMessageMixin,
                          LoginRequiredMixin, UpdateView):
    model = Teacher
    form_class = CabinetEditForm
    template_name = 'cabinet_edit.html'
    success_url = reverse_lazy('cabinet:edit-profile')
    success_message = _('Изменения успешно сохранены')

    def get_object(self, queryset=None):
        return self.request.user

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        context_data['is_email_confirmed'] = True if self.get_object().email_verification else False
        return context_data


class TeachingMaterialCreateView(CreateView):
    model = TeachingMaterial
    template_name = 'add_teaching_material.html'
    success_url = reverse_lazy('cabinet:index')
    fields = ('name', 'description', 'type', 'target_file')


class TeachingMaterialListView(ListView):
    model = TeachingMaterial
    template_name = 'teaching_materials_list.html'


class ScientificMaterialCreateView(CreateView):
    model = ScientificMaterial
    template_name = 'add_scientific_material.html'
    success_url = reverse_lazy('cabinet:index')
    fields = ('name', 'description', 'type', 'target_file')


class ScientificMaterialListView(ListView):
    model = ScientificMaterial
    template_name = 'scientific_materials_list.html'
