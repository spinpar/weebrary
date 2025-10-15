from django.urls import path
from . import views

urlpatterns = [
    path('', views.homepage, name='homepage'),
    path('anime/', views.fetch_anime, name='fetch_anime'),
    path('manga/', views.fetch_manga, name='fetch_manga'),
]
