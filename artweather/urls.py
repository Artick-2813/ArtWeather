
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('delete/', views.delete, name='delete'),
    path('app/', views.app, name='app')

]