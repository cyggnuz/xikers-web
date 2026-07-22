from django.urls import path
from . import views

app_name = 'music_bot'

urlpatterns = [
    path('recommend/', views.recommend_song, name='recommend_song'),
]