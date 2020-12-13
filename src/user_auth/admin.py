from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import Group

from user_auth.models import Teacher


@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
    pass


# unregistering unused model
admin.site.unregister(Group)

admin.register(UserAdmin, Teacher)
