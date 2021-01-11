from django.urls import path

from cabinet import views


app_name = 'cabinet'

urlpatterns = [
    path('', views.CabinetMainPageView.as_view(), name='index'),
    path('edit/', views.CabinetEditPageView.as_view(), name='edit-profile'),
    path('add_teching_material/', views.TeachingMaterialCreateView.as_view(), name='add-teaching-material'),
    path('teaching_materials/', views.TeachingMaterialListView.as_view(), name='teaching-materials')
]
