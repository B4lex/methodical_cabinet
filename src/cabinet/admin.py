from django.contrib import admin

from cabinet.models import (TeachingMaterial, ScientificMaterial,
                            TeachingMaterialType, ScientificMaterialType)


@admin.register(TeachingMaterial)
class TeachingMaterialAdmin(admin.ModelAdmin):
    pass


@admin.register(ScientificMaterial)
class ScientificMaterial(admin.ModelAdmin):
    pass


@admin.register(TeachingMaterialType)
class TeachingMaterialType(admin.ModelAdmin):
    pass


@admin.register(ScientificMaterialType)
class ScientificMaterialType(admin.ModelAdmin):
    pass
