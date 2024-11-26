from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('criarlista', views.criarlista, name='criarlista')
]