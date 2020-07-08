from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home, name="bot-home"),
    path('about/', views.about, name="bot-about"),
]
