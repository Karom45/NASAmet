from NASAmet.apps.accounts.views import redirect_view
from django.urls import path, include
from . import views


app_name = 'meteorites'
urlpatterns = [
    path('', redirect_view, name='index'),
    path('meteorites_list/<int:meteor_id>', views.detail_met, name='detail_met'),
    path('meteorites_list', views.meteorites_list, name='meteorites_list'),
    path('classes_list', views.classes_list, name='classes_list'),
    path('classes_list/<int:classes_id>', views.detail_class, name='detail_class'),
    path('classes_list/<int:classes_id>/change_class', views.change_class, name='change_class'),
    path('add_class', views.add_class, name='add_class'),
    path('classes_list/<int:classes_id>/delete_class', views.delete_class, name='delete_class'),
    path('add_meteorite', views.add_meteorite, name='add_meteorite'),
    path('meteorites_list/<int:meteor_id>/change_meteorite', views.change_meteorite, name='change_meteorite'),
    path('meteorites_list/<int:meteor_id>/delete_meteorite', views.delete_meteorite, name='delete_meteorite'),
]