from django.urls import path #re_path

from . import views


app_name = 'squirrels'

urlpatterns = [
    path('', views.index),
    path('<int:s_id>/', views.id_detail, name = 'id_detail'),
    path('add/',views.add_detail),
    path('stats/', views.stats),
   # path('<str:sighting_id>/', views.update, name='update'),#for update
    path('<squirrel_id>/',views.update, name = 'update'),
   # re_path(r'(?P<user_id>[0-9]+[A-Z]-[A-Z]{2}-[0-9]{4}-[0-9]{2})/', views.update),
]
