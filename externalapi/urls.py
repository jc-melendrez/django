from django.urls import path
from .import views

urlpatterns = [
    path('dog/', views.dog_api, name='dog_api'),
    path('cat/', views.cat_api, name='cat_api'),
    path('weather/', views.weather_api, name='weather_api'),
    path('joke/', views.joke_api, name='joke_api'),
    path('cat_img/', views.cat_img_api, name='cat_img'),
    path('duck_img/', views.duck_api, name='duck_img'),
    path('fox_img/', views.fox_api, name='fox_img'),


]