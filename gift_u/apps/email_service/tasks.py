from celery import shared_task 
from django.core.mail import send_mail

@shared_task
def send_email_task():
    send_mail('hello','this is a test message, Just Shut up','ntustartup2019@gmail.com',['ivan861118@gmail.com'], fail_silently=False)
    return 'Task Completed!'