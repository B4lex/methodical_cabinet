from django.db import models


class QualificationCategory(models.Model):
    title = models.CharField(max_length=255)


class TeachingRank(models.Model):
    title = models.CharField(max_length=255)


class Subject(models.Model):
    title = models.CharField(max_length=255)


class AbstractMaterial(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    user = models.ForeignKey('user_auth.Teacher', on_delete=models.SET_NULL, blank=True, null=True)
    target_file = models.FileField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    class Meta:
        abstract = True


class TeachingMaterial(AbstractMaterial):
    type = models.ForeignKey('cabinet.TeachingMaterialType', on_delete=models.SET_NULL, null=True)


class ScientificMaterial(AbstractMaterial):
    type = models.ForeignKey('cabinet.ScientificMaterialType', on_delete=models.SET_NULL, null=True)


class TeachingMaterialType(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class ScientificMaterialType(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name
