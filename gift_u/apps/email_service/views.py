from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
from .tasks import send_email_task

def sendmail(request):
    send_email_task.delay()
    return HttpResponse('<h1>EMAIL HAS BEEN SENT WITH CELERY!</h1>')
