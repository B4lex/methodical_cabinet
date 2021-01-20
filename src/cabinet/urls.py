from django.conf.urls.static import static
from django.conf import settings
from django.urls import path

from cabinet import views


app_name = 'cabinet'

urlpatterns = [
    path('', views.CabinetMainPageView.as_view(), name='index'),
    path('edit/', views.CabinetEditPageView.as_view(), name='edit-profile'),
    path('add_teching_material/', views.TeachingMaterialCreateView.as_view(), name='add-teaching-material'),
    path('teaching_materials/', views.TeachingMaterialListView.as_view(), name='teaching-materials'),
    path('add_scientific_material/', views.ScientificMaterialCreateView.as_view(), name='add-scientific-material'),
    path('scientific_materials/', views.ScientificMaterialListView.as_view(), name='scientific-materials'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
