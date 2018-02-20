from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('filter/<int:id>/', views.filter, name='filter'),
    path('filter/<int:id>/<str:metal_name>/', views.filter, name='filter_metal'),
]