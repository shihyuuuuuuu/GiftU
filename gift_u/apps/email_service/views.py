from django.shortcuts import render
from django.http import HttpResponse

from .utils import encode, decode


# Create your views here.
from .tasks import send_email_task

def index(request):
    if request.method == 'POST':
        
        data = request.POST
        print(data)
        # Todo: 用serializer做驗證
        is_reply = True if data['is_reply'] == 'true' else False
        if is_reply:
            sender = decode(data['sender'])
            recipient = decode(data['recipient'])

            reply_link = None #回信不能再回覆
        else:
            sender = data['sender']
            if sender == '': sender = None #should be moved to serializer logic
            recipient = data['recipient']

            reply_link = f"https://giftu.herokuapp.com/email_service/?sender={encode(sender)}&recipient={encode(recipient)}" if sender else None #寄信時有提供email，才會有回覆連結
        
        sender_info = {
            "sender_name": sender.split('@')[0] if sender else '匿名使用者',
            "anonymous": True if data['anonymous'] == 'true' else False,
        }   

        send_email_task.delay(sender_info=sender_info, recipient=recipient, title=data['title'], message=data['message'], reply_link=reply_link)
        return HttpResponse('<h1>感謝您使用本服務，信件已經寄出囉！</h1>')
    else:
        sender = request.GET.get("sender")
        recipient = request.GET.get("recipient")
        if sender and recipient:
            return render(request, 'email_service/reply_mail.html',context={"sender":sender, "recipient":recipient})

        return render(request, 'email_service/sender_mail.html',{})
    


        
