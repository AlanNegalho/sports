from django.urls import path
from . import views

urlpatterns = [
    path('', views.atletas, name='atletas'),
    path('create/', views.create, name='create'),
    path('update/<int:id>/', views.update, name='update'),
    path('delete/<int:id>/', views.delete, name='delete'),
    # Times
    path('times/', views.times, name='times'),
    path('ceate_time/', views.create_time, name='create_time'),
    path('update_time/<int:id>/',views.update_time, name='update_time'),
    path('delete_time/<int:id>/', views.delete_time, name= 'delete_time'),
    
]