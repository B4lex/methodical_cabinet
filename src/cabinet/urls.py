from django.urls import path

from cabinet import views


urlpatterns = [
    path('', views.CabinetMainPageView.as_view(), name='cabinet-index'),
    path('edit/', views.CabinetEditPageView.as_view(), name='cabinet-edit')
]
