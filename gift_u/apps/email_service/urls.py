from django.urls import include, path
from . import views ## For baseDir 

urlpatterns = [
    path('', views.index, name='index'),
]