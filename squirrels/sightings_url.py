from django.urls import path

from . import views

urlpatterns = [
    path('', views.index),
   # path('<str:sighting_id>/', views.id_detail),
    path('add/',views.add_detail),
    path('stats/', views.stats),
]
