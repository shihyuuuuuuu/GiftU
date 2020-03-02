from django.shortcuts import render, redirect
# models
from .models import Questionnaire, ChoiceQuestion, Choice, AnswerSheet, ChoiceAnswer
# views
from django.views.generic import View
# forms
from .forms import QuestionnaireForm, ChoiceQuestionForm, ChoiceFormset, AnswerSheetForm

# For email
from django.conf import settings
from django.core.mail import BadHeaderError, send_mail
from django.http import HttpResponse

class SurveyView(View):
    def get(self, request):
        current_user = request.user
        
        # Empty questionnaire
        questionnaire_form = QuestionnaireForm(prefix='questionnaire')
        choice_formset = ChoiceFormset(prefix='choice', initial=[
            {'order_in_list':i+1} for i in range(3)])
        context = {
            'questionnaire_form':questionnaire_form,
            'choice_formset':choice_formset,
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
<<<<<<< Updated upstream
                self.send_email(current_user.username, questionnaire.receiver_nickname)
                
                # Create an empty answersheet for future response
                answersheet = AnswerSheet.objects.create(questionnaire=questionnaire)
=======

                # shanpig : Add data format sent to send_email()
                data = [
                    questionnaire.receiver_email,       #收信人信箱
                    questionnaire.sender_nickname,      #寄信人
                    questionnaire.receiver_nickname,    #收信人
                    questionnaire.extra_messages,       #想說的話
                    ]

                # self.send_email(current_user.username, questionnaire.receiver_nickname)
                self.send_email(data)
>>>>>>> Stashed changes
                return redirect('/', {})
        else:
            print("Questionnaire %s submit failed ! "%questionnaire.id)
        return redirect('/survey/')
    
    def send_email(self, data): # sender receiver
        from django.template.loader import render_to_string
        from django.utils.html import strip_tags
        
        subject = "Email testing!"
        html_context = {
            # 'sender':sender,
            # 'receiver':receiver
            'sender' : data[1],
            'receiver' : data[2],
            'message' : data[3]
        }
        html_message = render_to_string('survey/questionnaire_mail.html', html_context)
        plain_message = strip_tags(html_message)
        
        from_email = settings.EMAIL_HOST_USER
        # to_email = 'b05203008@ntu.edu.tw'
        to_email = data[0]
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
            

    def post(self, request, questionnaire_id=''):
        current_user = request.user
        questionnaire = Questionnaire.objects.filter(id=questionnaire_id).get()

        ## Parse data
        choice_pk = request.POST.get('answersheet-choices')
        extra_messages = request.POST.get('answersheet-extra_messages')


        answer_sheet = AnswerSheet.objects.filter(questionnaire=questionnaire).get() ##
        answer_sheet.extra_messages = extra_messages
        answer_sheet.done = True
        answer_sheet.save()

        choice = Choice.objects.filter(pk=choice_pk).get()
        choice_answer = ChoiceAnswer.objects.create(
            answer_sheet=answer_sheet,
            choice_question=choice.choice_question,
            choice=choice
        )

        questionnaire.is_responded = True
        questionnaire.save()

        return redirect('/accounts/dashboard')
    
    def get_questionnaire_with_id(self, current_user, questionnaire_id):
        questionnaire = Questionnaire.objects.filter(id=questionnaire_id).get()
        
        context = {}

        # Check authorized
        if (current_user.email != questionnaire.creator.email and current_user.email != questionnaire.receiver_email):
            return context
        
        questionnaire_form = QuestionnaireForm(prefix='questionnaire', instance=questionnaire)
        choice_question = ChoiceQuestion.objects.filter(questionnaire=questionnaire).get()
        choice_formset = ChoiceFormset(prefix='choice', instance=choice_question)

        answersheet = AnswerSheet.objects.filter(questionnaire=questionnaire).get()
        choice_answer = ''

        if questionnaire.is_responded:
            choice_answer = ChoiceAnswer.objects.filter(choice_question=choice_question).get()
            answersheet_form = AnswerSheetForm(questionnaire=questionnaire, prefix='answersheet')
        else:
            answersheet_form = AnswerSheetForm(questionnaire=questionnaire, prefix='answersheet' )

        context = {
            'questionnaire':questionnaire,
            'questionnaire_form':questionnaire_form,
            'choice_formset':choice_formset,
            'answersheet':answersheet,
            'answersheet_form':answersheet_form,
            'choice_answer':choice_answer,
        }
        return context

# def index(request):
#     latest_question_list = Question.objects.order_by('-pub_date')[:5]
#     context = {'latest_question_list': latest_question_list}
#     return render(request, 'polls/index.html', context)

# Deprecated
# def demo(request):
#     return render(request, 'survey/demo.html', {})