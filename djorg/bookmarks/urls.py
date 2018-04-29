from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name = 'index')
]

# This matches a path to the view