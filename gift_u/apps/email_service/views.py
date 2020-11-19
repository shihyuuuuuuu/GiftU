from django.shortcuts import render
from django.http import HttpResponse

from .utils import decode


# Create your views here.
from .tasks import send_email_task

def index(request):
    if request.method == 'POST':
        
        data = request.POST
        # Todo: 用serializer
        sender = decode(data['sender']) if data['is_reply'] == True else data['sender']
        if sender == '': sender = None #should be moved to serializer logic
        recipient = decode(data['recipient']) if data['is_reply'] == True else data['recipient']
        anonymous = True if data['anonymous'] == 'true' else False

        send_email_task.delay(sender=sender, recipient=recipient, title=data['title'], message=data['message'], anonymous=anonymous)
        return HttpResponse('<h1>感謝您使用本服務，信件已經寄出囉！</h1>')
    else:
        sender = request.GET.get("sender")
        recipient = request.GET.get("recipient")
        if sender and recipient:
            return render(request, 'email_service/reply_mail.html',context={"sender":sender, "recipient":recipient})

        return render(request, 'email_service/sender_mail.html',{})
    


        
