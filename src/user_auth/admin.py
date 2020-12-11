from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from user_auth.models import Teacher


@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
    pass


admin.register(UserAdmin, Teacher)
