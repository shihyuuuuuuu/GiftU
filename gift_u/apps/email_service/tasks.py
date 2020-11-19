from celery import shared_task 
from django.core.mail import send_mail
from django.template.loader import render_to_string
from .utils import encode

@shared_task
def send_email_task(sender_info: dict, recipient: str, title: str, message:str, reply_link: str=None):
    """
    sender_info = {
        sender_name: str,
        anonymous: bool,
    }
    """
    if sender_info['sender_name'] and not sender_info['anonymous']:
        sender = sender_info['sender_name']
    else:
        sender = '匿名使用者'

    html_message = render_to_string('email_service/email_template.html',  {
        'title':title,
        'message':message,
        'reply_link':reply_link
    })

    send_mail(title, message, f"{sender} 透過 心禮系<ntustartup2019@gmail.com>", [recipient], fail_silently=False, html_message=html_message)
    return 'Task Completed!'