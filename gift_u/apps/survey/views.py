from django.shortcuts import render, redirect
# models
from .models import Questionnaire, ChoiceQuestion, Choice
# views
from django.views.generic import View
# forms
from .forms import QuestionnaireForm, ChoiceQuestionForm, ChoiceFormset

# For email
from django.conf import settings
from django.core.mail import BadHeaderError, send_mail
from django.http import HttpResponse

class SurveyView(View):
    def get(self, request):
        current_user = request.user
        
        # Empty questionnaire
        questionnaire_form = QuestionnaireForm(prefix='questionnaire')
        choice_formset = ChoiceFormset(prefix='choice')
        context = {
            'questionnaire_form':questionnaire_form,
            'choice_formset':choice_formset,
            'read_only': False
        }
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
                self.send_email(current_user.username, questionnaire.receiver_nickname)
                return redirect('/', {})
        else:
            print("Questionnaire %s submit failed ! "%questionnaire.id)
        return redirect('/survey/')
    
    def send_email(self, sender, receiver):
        from django.template.loader import render_to_string
        from django.utils.html import strip_tags
        
        subject = "Email testing!"
        html_context = {
            'sender':sender,
            'receiver':receiver
        }
        html_message = render_to_string('survey/questionnaire_mail.html', html_context)
        plain_message = strip_tags(html_message)
        
        from_email = settings.EMAIL_HOST_USER
        to_email = 'b05901018@ntu.edu.tw'
        if subject and html_message and from_email:
            try:
                send_mail(subject, plain_message, from_email, [to_email], False, html_message=html_message)
            except BadHeaderError:
                return HttpResponse('Invalid header found.')
            return redirect('/', {})
        else:
            # In reality we'd use a form class
            # to get proper validation errors.
            return HttpResponse('Make sure all fields are entered and valid.')

        return False

class QuestionnaireView(View):
    def get(self, request, questionnaire_id=''):
        current_user = request.user
        
        # Get user's specific questionnaire
        context = self.get_questionnaire_with_id(current_user, questionnaire_id)
        return render(request, 'survey/questionnaire.html', context)
            

    def post(self, request):
        current_user = request.user
        questionnaire_form = QuestionnaireForm(request.POST, prefix='questionnaire', initial={'creator':current_user})

        return redirect('/survey/')
    
    def get_questionnaire_with_id(self, current_user, questionnaire_id):
        questionnaire = Questionnaire.objects.filter(id=questionnaire_id).get()
        
        context = {}
        # Check authorized
        if (current_user == questionnaire.creator or
        current_user.email == questionnaire.receiver_email):
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