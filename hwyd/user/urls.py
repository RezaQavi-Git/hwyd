from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='Home'),
    path('users/', views.users, name='users'),
    path('login', views.login, name='login'),
    path('signup', views.signup, name='signup'),
    path('rate', views.rate, name='rate'),
    path('logout/', views.logout, name='logout'),
]