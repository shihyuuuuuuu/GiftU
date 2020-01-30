from django.shortcuts import render, redirect
# models
from .models import Questionnaire, ChoiceQuestion, Choice
# views
from django.views.generic import View
# forms
from .forms import QuestionnaireForm, ChoiceQuestionForm, ChoiceFormset

class QuestionnaireView(View):
    
    def get(self, request, username='admin'):
        questionnaire_form = QuestionnaireForm(prefix='questionnaire')
        choice_formset = ChoiceFormset(prefix='choice')
        context = {
            'questionnaire_form':questionnaire_form,
            'choice_formset':choice_formset
        }
        return render(request, 'survey/survey.html', context)

    def post(self, request):
        current_user = request.user
        questionnaire_form = QuestionnaireForm(request.POST, prefix='questionnaire', initial={'creator':current_user})

        if questionnaire_form.is_valid():
            ## inline formset 的做法
            questionnaire = questionnaire_form.save()
            print("Questionnaire %s submit success"%questionnaire.id)

            choice_question = ChoiceQuestion.objects.create(questionnaire=questionnaire)
            choice_formset = ChoiceFormset(request.POST, prefix='choice')
            if choice_formset.is_valid():
                instances = choice_formset.save(commit=False)
                for instance in instances:
                    instance.choice_question = choice_question
                    instance.save()

        return redirect('/', {})

        

# def index(request):
#     latest_question_list = Question.objects.order_by('-pub_date')[:5]
#     context = {'latest_question_list': latest_question_list}
#     return render(request, 'polls/index.html', context)

# Deprecated
# def demo(request):
#     return render(request, 'survey/demo.html', {})
