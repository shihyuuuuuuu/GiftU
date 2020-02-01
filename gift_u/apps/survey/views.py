from django.shortcuts import render, redirect
# models
from .models import Questionnaire, ChoiceQuestion, Choice
# views
from django.views.generic import View
# forms
from .forms import QuestionnaireForm, ChoiceQuestionForm, ChoiceFormset

class QuestionnaireView(View):
    
    def get(self, request, questionnaire_id=''):
        current_user = request.user
        
        # Empty questionnaire
        if not questionnaire_id:
            questionnaire_form = QuestionnaireForm(prefix='questionnaire')
            choice_formset = ChoiceFormset(prefix='choice')
            context = {
                'questionnaire_form':questionnaire_form,
                'choice_formset':choice_formset,
                'read_only': False
            }
            
        # Get user's specific questionnaire
        else:
            context = self.get_questionnaire_with_id(current_user, questionnaire_id)
        return render(request, 'survey/survey.html', context)
            

    def post(self, request):
        current_user = request.user
        questionnaire_form = QuestionnaireForm(request.POST, prefix='questionnaire', initial={'creator':current_user})

        if questionnaire_form.is_valid():
            ## First, create a questionnaire
            questionnaire = questionnaire_form.save()
            print("Questionnaire %s submit success !"%questionnaire.id)

            ## Then, create a choice_question relate to questionnaire
            choice_question = ChoiceQuestion.objects.create(questionnaire=questionnaire)
            choice_formset = ChoiceFormset(request.POST, prefix='choice', instance=choice_question)
            if choice_formset.is_valid():
                choice_formset.save()
                return redirect('/', {})
        else:
            print("Questionnaire %s submit failed ! "%questionnaire.id)
        return redirect('/survey/')
    
    def get_questionnaire_with_id(self, current_user, questionnaire_id):
            questionnaire = Questionnaire.objects.filter(id=questionnaire_id).get()
            
            # Check authorized
            if current_user == questionnaire.creator:
                questionnaire_form = QuestionnaireForm(prefix='questionnaire', instance=questionnaire)

                choice_question = ChoiceQuestion.objects.filter(questionnaire=questionnaire).get()
                choice_formset = ChoiceFormset(prefix='choice', instance=choice_question)
            
                context = {
                    'questionnaire_form':questionnaire_form,
                    'choice_formset':choice_formset,
                    'read_only': True,
                }
            return context

        

# def index(request):
#     latest_question_list = Question.objects.order_by('-pub_date')[:5]
#     context = {'latest_question_list': latest_question_list}
#     return render(request, 'polls/index.html', context)

# Deprecated
# def demo(request):
#     return render(request, 'survey/demo.html', {})
