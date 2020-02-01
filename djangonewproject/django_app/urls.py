from django.contrib import admin
from django.urls import path
from .import views
app_name = 'django_app'
from.views import (
    index,  
    loginView,
    get_logout,  
    get_register
)

urlpatterns = [
    path('', views.index, name='index'),
    path('login/', views.loginView, name='login'),
    path('logout/', views.get_logout, name="logout"),
    path('register/', views.get_register, name="register")
]