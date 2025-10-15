# from django.urls import render
from django.urls import path

from . import views 

urlpatterns = [
    path("", views.homepage, name="homepage"),
#    path("button/", views.api_button, name="button_action"),
]