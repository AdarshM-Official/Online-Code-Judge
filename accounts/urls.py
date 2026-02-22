from django.urls import path, include
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('signup/', views.signup, name='signup'),
    # This includes login, logout, password resets, etc.
    path('', include('django.contrib.auth.urls')), 
]