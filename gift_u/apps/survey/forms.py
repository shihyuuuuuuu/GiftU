from django import forms
from .models import Questionnaire, ChoiceQuestion, Choice

from django.forms import inlineformset_factory


class QuestionnaireForm(forms.ModelForm):
    class Meta:
        model = Questionnaire
        exclude = ['creator']
        labels = {
            'receiver_email': '收禮者的email',
            'receiver_nickname': '你想要如何稱呼對方',
            'sender_nickname': '你的暱稱（可以透露一點訊息給對方）',
        }


class ChoiceQuestionForm(forms.ModelForm):
    class Meta:
        model = ChoiceQuestion
        fields = '__all__'

# ChoiceQuestionFormset = inlineformset_factory(Questionnaire, ChoiceQuestion, fields=('__all__'))
ChoiceFormset = inlineformset_factory(ChoiceQuestion, Choice, fields=('choice_text',), can_delete = False)

