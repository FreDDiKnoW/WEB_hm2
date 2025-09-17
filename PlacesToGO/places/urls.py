from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('all_places/', views.all_places, name='all_places'),
    path('add_place/', views.add_place, name='add_place'),
    path('where_to_go/', views.where_to_go, name='where_to_go'),
]
