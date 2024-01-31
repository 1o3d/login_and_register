from django.urls import path, include
from .views import register
from . import views
from django.contrib.auth import logout

urlpatterns = [
    # path('/register', views.register, name='register')
    path('home/', views.home, name='home'),
    path('', include('django.contrib.auth.urls')),
    path('register/', register, name='register'),
    path('profile/', views.profile, name='profile'),
    path('profile/home/', views.your_profile, name='login'),
    path('logout', views.log_out_view, name='logout',),
    path('contact/', views.contact_view, name='contact'),
    path('clipboard/', views.clipboard, name='clipboard')
]