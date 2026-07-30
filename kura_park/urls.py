from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_view, name='home'),
    path('park/', views.park_view, name='park'),
    path('museum/', views.museum_view, name='museum'),
    path('temple/', views.temple_view, name='temple'),
    path('thermal/', views.thermal_view, name='thermal'),
    path('about/', views.about_view, name='about'),
    path('map/', views.map_view, name='map'),
    path('contacts/', views.contacts_view, name='contacts'),
    path('old-oak/', views.old_oak_view, name='old_oak'),
]