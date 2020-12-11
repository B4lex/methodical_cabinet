from django.db import models


class QualificationCategory(models.Model):
    title = models.CharField(max_length=255)


class TeachingRank(models.Model):
    title = models.CharField(max_length=255)


class Subject(models.Model):
    title = models.CharField(max_length=255)
