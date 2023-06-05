from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('users', views.users, name='users'),
    path('login', views.login, name='login'),
    path('signup', views.signup, name='signup'),
    path('rate', views.rate, name='rate'),
    path('history', views.history, name='history'),
    path('test', views.test, name='test'),

]