from celery import shared_task 
from django.core.mail import send_mail

@shared_task
def send_email_task(recipient, title, message):
    send_mail(title, message,'ntustartup2019@gmail.com',[recipient], fail_silently=False)
    return 'Task Completed!'