from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='blog-home'),
    path('about/', views.about, name='blog-about'),

    path('benon/', views.benon, name='blog-benon'),
    path('benon/asd/', views.benon_asd, name='blog-benon-asd'),
]