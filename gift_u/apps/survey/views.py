from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse

from .models import Questionnaire, Question


def index(request, creator='admin', question_id='0'):
    # questionnaire = Questionnaire.objects.filter(creator=creator).order_by('id')
    # questionnaire = Questionnaire.objects.all()

    return render(request, 'survey/survey.html', {'questionnaire':questionnaire})

# def index(request):
#     latest_question_list = Question.objects.order_by('-pub_date')[:5]
#     context = {'latest_question_list': latest_question_list}
#     return render(request, 'polls/index.html', context)

def demo(request):
    return render(request, 'survey/demo.html', {})
