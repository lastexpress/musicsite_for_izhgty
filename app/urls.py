from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from . import views

app_name = 'app'

urlpatterns = [
	path('', views.MainScreen, name="MainScreen"),
	path('genre/<str:name>/', views.GenreDetail, name='genre_detail'),
	path('album/<str:slug>', views.AlbumDetail, name='album_detail'),

]