from celery import shared_task 
from django.core.mail import send_mail
from django.template.loader import render_to_string
from .utils import encode

@shared_task
def send_email_task(recipient, title, message, sender=None):
    if sender:
        sender = encode(sender) 
        html_message = render_to_string('email_service/email_template.html',  {
            'title':title,
            'message':message,
            'reply_link':f"https://giftu.herokuapp.com/email_service/?recipient={sender}"
        })
    else:
        html_message = render_to_string('email_service/email_template.html',  {
            'title':title,
            'message':message,
            'reply_link':None
        })
    send_mail(title, message,'心禮系<ntustartup2019@gmail.com>',[recipient], fail_silently=False, html_message=html_message)
    return 'Task Completed!'