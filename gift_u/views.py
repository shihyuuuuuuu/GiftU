from django.shortcuts import render, redirect

# Create your views here.

from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, logout, authenticate

def index(request):
    if request.user.is_authenticated:
        return redirect('/home')
    return render(request, 'landing_page.html', locals())

    
def home(request):
    return render(request, 'home_page.html', locals())


def profile(request):
    return render(request, 'profile.html', locals())



    
