from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    # path('login/', views.login, name='login'),
    path('', views.home, name='home'),
    # path('register/', views.register, name='register')
    path('child/', views.child, name='child')
]