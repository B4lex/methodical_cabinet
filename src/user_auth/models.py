from django.contrib.auth.models import AbstractUser
from django.db import models


class Teacher(AbstractUser):
    full_name = models.CharField(max_length=255)
    email = models.EmailField()
    email_verification = models.DateTimeField()
    photo = models.ImageField()
    qualification_category = models.ForeignKey(
        'cabinet.QualificationCategory',
        on_delete=models.SET_NULL,
        null=True
    )
    teaching_rank = models.ForeignKey(
        'cabinet.TeachingRank',
        on_delete=models.SET_NULL,
        null=True
    )
    experience = models.DurationField()
    subject = models.ForeignKey(
        'cabinet.Subject',
        on_delete=models.SET_NULL,
        null=True
    )
    awards = models.TextField()
    social_networks_link = models.URLField(blank=True, null=True)  # may need to be used with Postgres ArrayField
    youtube_link = models.URLField(blank=True, null=True)
