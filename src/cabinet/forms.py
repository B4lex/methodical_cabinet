from django import forms
from user_auth.models import Teacher


class CabinetEditForm(forms.ModelForm):

    class Meta:
        model = Teacher
        exclude = (
            'first_name', 'last_name', 'date_joined',
            'password', 'last_login', 'is_superuser', 'groups',
            'username', 'is_staff', 'is_active', 'user_permissions'
        )
