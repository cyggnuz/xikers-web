from django.urls import path
from . import views

app_name = 'members'

urlpatterns = [
    # /members/  -> muestra el primer integrante por defecto
    path('', views.member_detail, name='list'),
    # /members/3/ -> muestra el integrante con id 3
    path('<int:pk>/', views.member_detail, name='detail'),
]