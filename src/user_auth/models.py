from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _


class Teacher(AbstractUser):
    full_name = models.CharField(max_length=255, null=True)
    email = models.EmailField(error_messages={
        'unique': _('Пользователь с таким электронным адресом уже существует')
        }, unique=True, null=True, blank=True)
    email_verification = models.DateTimeField(null=True, blank=True)
    photo = models.ImageField(null=True, blank=True)
    qualification_category = models.ForeignKey(
        'cabinet.QualificationCategory',
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )
    teaching_rank = models.ForeignKey(
        'cabinet.TeachingRank',
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )
    experience = models.DurationField(null=True)
    subject = models.ForeignKey(
        'cabinet.Subject',
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )
    awards = models.TextField(blank=True, null=True)
    social_networks_link = models.URLField(blank=True, null=True)  # may need to be used with Postgres ArrayField
    youtube_link = models.URLField(blank=True, null=True)

    class Meta:
        verbose_name = _('Преподаватель')
        verbose_name_plural = _('Преподаватели')
