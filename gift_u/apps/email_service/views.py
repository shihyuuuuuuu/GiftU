from django.shortcuts import render
from django.http import HttpResponse

from .utils import decode


# Create your views here.
from .tasks import send_email_task

def index(request):
    if request.method == 'POST':
        data = request.POST
        recipient = decode(data['recipient']) if request.POST.get('anonymous') else data['recipient']

        send_email_task.delay(sender=data['sender'], recipient=recipient, title=data['title'], message=data['message'])
        return HttpResponse('<h1>感謝您使用本服務，信件已經寄出囉！</h1>')
    else:
        recipient = request.GET.get("recipient")
        return render(request, 'email_service/send_mail.html',context={"recipient":recipient})
    


        
