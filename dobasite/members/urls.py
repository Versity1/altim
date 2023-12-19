from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='Home'),
    path('login/', views.login, name='login'),
    path('register/', views.register, name='register'),
    path('profile/', views.profile, name='profile'),
    path('table/', views.table, name='Details'),
]