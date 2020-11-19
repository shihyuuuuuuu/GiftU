from celery import shared_task 
from django.core.mail import send_mail
from django.template.loader import render_to_string
from .utils import encode

@shared_task
def send_email_task(sender, recipient, title, message, anonymous=True):
    sender_name = sender.split('@')[0] if (sender and not anonymous) else '匿名使用者'
    reply_link = f"https://giftu.herokuapp.com/email_service/?sender={encode(sender)}&recipient={encode(sender)}" if sender else None #寄信時有提供email，才會有回覆連結
    
    html_message = render_to_string('email_service/email_template.html',  {
        'title':title,
        'message':message,
        'reply_link':reply_link
    })

    send_mail(title, message,f'{sender_name} 透過 心禮系<ntustartup2019@gmail.com>',[recipient], fail_silently=False, html_message=html_message)
    return 'Task Completed!'