from django.urls import path
from . import views


# all urls patterns are collected here for routing to the different view functions defined in views.py
urlpatterns = [
    path('', views.index),
    path('new', views.new)
]