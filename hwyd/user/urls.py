from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('login', views.login, name='login'),
    path('logout', views.logout, name='logout'),
    path('signup', views.signup, name='signup'),
    path('rate', views.rate, name='rate'),
    path('history', views.history, name='history'),
    path('test', views.test, name='test'),

]