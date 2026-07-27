from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('news/<int:pk>/', views.news_detail, name='news_detail'),  # НАШ НОВЫЙ ДИНАМИЧЕСКИЙ ПУТЬ
    path('museum/', views.museum, name='museum'),
    path('about/', views.about, name='about'),
    path('thermal/', views.thermal, name='thermal'),
    path('temple/', views.temple, name='temple'),
    path('contacts/', views.contacts, name='contacts'),
    
    # МАРШРУТЫ ДЛЯ ИНТЕРАКТИВНОЙ КАРТЫ
    path('map/', views.map_view, name='map'),
    path('api/marks/', views.get_marks, name='get_marks'),
    path('api/marks/add/', views.add_mark, name='add_mark'),
]