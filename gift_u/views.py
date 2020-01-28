from django.shortcuts import render, redirect

# Create your views here.

from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, logout, authenticate

## python package
import logging


def index(request):
    return render(request, 'homepage.html', locals())

## Deprecated after allauth

# def register(request):
#     if request.method == 'POST':
#         form = UserCreationForm(request.POST)
#         if form.is_valid():
#             user = form.save()
            
#             username = form.cleaned_data.get('username')
#             raw_password = form.cleaned_data.get('password1')
#             user = authenticate(username=username, password=raw_password)
#             login(request, user)
#             return redirect('homepage')
#         else:
#             for msg in form.error_messages: # "msg" is the key
#                 logging.error(form.error_messages[msg])

#     form = UserCreationForm
#     return render(request, 'registration/register.html', context={"form":form})

def profile(request):
    return render(request, 'profile.html', locals())
