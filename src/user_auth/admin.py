from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import Group
from django.utils.translation import gettext_lazy as _

from user_auth.models import Teacher


@admin.register(Teacher)
class TeacherAdmin(UserAdmin):
    fieldsets = (
        (None, {'fields': ('password',)}),
        (_('Personal info'), {'fields': ('full_name', 'email', 'photo', 
                                         'qualification_category', 'teaching_rank', 
                                         'experience', 'subject', 'awards', 
                                         'social_networks_link', 'youtube_link')}),
        (_('Permissions'), {
            'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions'),
        }),
        (_('Important dates'), {'fields': ('last_login', 'date_joined', 'email_verification')}),
    )

    list_display = ('full_name', 'email',)
    ordering = ('full_name',)
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('full_name', 'password1', 'password2'),
        }),
    )


# unregistering unused model
admin.site.unregister(Group)
