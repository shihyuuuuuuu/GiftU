from django import forms
from .models import Questionnaire, ChoiceQuestion, Choice

from django.forms import inlineformset_factory


class QuestionnaireForm(forms.ModelForm):
    class Meta:
        model = Questionnaire
        fields = [
            'receiver_email', 
            'receiver_nickname', 
            'sender_nickname',
            'extra_messages',
            ]
        labels = {
            'receiver_email': '收禮者的email',
            'receiver_nickname': '你想要如何稱呼對方',
            'sender_nickname': '你的暱稱（可以透露一點訊息給對方）',
            'extra_messages': '你還想對她說什麼嗎？',
        }


class ChoiceQuestionForm(forms.ModelForm):
    class Meta:
        model = ChoiceQuestion
        fields = '__all__'
ChoiceFormset = inlineformset_factory(ChoiceQuestion, Choice, fields=('choice_text',), can_delete = False, max_num=3)

