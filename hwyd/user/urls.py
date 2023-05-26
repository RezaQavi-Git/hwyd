from django.urls import path
from . import views

urlpatterns = [
    path('users/', views.users, name='users'),
    path('rating/', views.rating, name='rating'),
]