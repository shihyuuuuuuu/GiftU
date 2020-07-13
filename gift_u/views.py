from django.shortcuts import render, redirect

# Create your views here.

from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, logout, authenticate

from survey.models import Questionnaire

def index(request):
    return render(request, 'homepage.html', locals())


def profile(request):
    return render(request, 'profile.html', locals())


def dashboard(request):
    current_user = request.user 
    questionnaires = Questionnaire.objects.filter(creator=current_user)
    return render(request, 'dashboard.html', {'questionnaires':questionnaires} )

    
