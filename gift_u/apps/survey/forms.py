from django import forms
from .models import Questionnaire, ChoiceQuestion, Choice, AnswerSheet

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
ChoiceFormset = inlineformset_factory(ChoiceQuestion, Choice, fields=('choice_text','order_in_list'), widgets = {'order_in_list': forms.HiddenInput()}, can_delete = False, max_num=3)

class AnswerSheetForm(forms.Form):
    choices = forms.ModelChoiceField(label='請在以下三個他提供的選項中，選擇你想要的', queryset=None, empty_label="選擇其中一個")
    extra_messages = forms.CharField(widget=forms.Textarea, label='回覆一些文字給他吧！')
    
    def __init__(self,*args, **kwargs):
        questionnaire = kwargs.pop('questionnaire', None)
        super(AnswerSheetForm, self).__init__(*args, **kwargs)
        self.fields['choices'].queryset = Choice.objects.filter(choice_question__questionnaire=questionnaire)
