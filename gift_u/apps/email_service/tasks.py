from django.core.mail import BadHeaderError, send_mail
from gift_u.celery import (
    app,
)

@app.task(bind=True)
def send_email(self):
    send_mail('hello','this is a test message','ntustartup2019@gmail.com',['ivan861118@gmail.com'], fail_silently=False)