from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse


def index(request):
    return render(request, 'survey/survey.html', {})

def demo(request):
    return render(request, 'survey/demo.html', {})
