from django.urls import path

from . import views


app_name = 'squirrels'

urlpatterns = [
    path('', views.index),
    path('<int:s_id>/', views.id_detail, name = 'id_detail'),
    path('add/',views.add_detail),
    path('stats/', views.stats),
]
