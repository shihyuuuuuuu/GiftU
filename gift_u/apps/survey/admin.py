from django.contrib import admin

# Register your models here.
from .models import *

admin.site.register(Questionnaire)
admin.site.register(ChoiceQuestion)
admin.site.register(AnswerSheet)
admin.site.register(ChoiceAnswer)
