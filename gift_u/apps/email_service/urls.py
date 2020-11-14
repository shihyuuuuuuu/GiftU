from django.urls import include, path
from . import views ## For baseDir 

urlpatterns = [
    path('sendmail', views.sendmail, name='sendmail'),
]