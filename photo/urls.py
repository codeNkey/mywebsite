from django.urls import path
from . import views

urlpatterns = [
  path('', views.photo_list, name='photo_list'),
  path('photo/<int:pk>/', views.photo_detail, name='photo_detail')
]