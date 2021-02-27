from django.urls import path, include
from . import views

app_name = 'meteorites'
urlpatterns = [
    path('', views.index, name='index'),
    path('meteorites_list/<int:meteor_id>', views.detail_met, name='detail_met'),
    path('meteorites_list', views.meteorites_list, name='meteorites_list'),
    path('classes_list', views.classes_list, name='classes_list'),
    path('classes_list/<int:classes_id>', views.detail_class, name='detail_class'),
]