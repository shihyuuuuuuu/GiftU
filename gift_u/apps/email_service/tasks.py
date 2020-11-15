from celery import shared_task 
from django.core.mail import send_mail
from django.template.loader import render_to_string

@shared_task
def send_email_task(recipient, title, message):
    html_message = render_to_string('email_service/email_template.html',  {
        'title':title,
        'message':message
    })
    send_mail(title, message,'ntustartup2019@gmail.com',[recipient], fail_silently=False, html_message=html_message)
    return 'Task Completed!'