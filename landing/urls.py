from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('calculate/', views.calculate, name='calculate'),
]
