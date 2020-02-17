from django.urls import path

from .views import (
    SurveyView,
    QuestionnaireView
)

# Can be used as : "{% url 'survey:index' %}"
app_name = 'survey'

urlpatterns = [
    # ex: /survey/
    path('', SurveyView.as_view(), name='index'),
    # ex: /survey/2
    path('<str:questionnaire_id>/', QuestionnaireView.as_view(), name='questionnaire'),
    # ex: /survey/5/response
    # path('<str:questionnaire_id>/response', views.response, name='response'),

    # Deprecated
    # path('demo', views.demo, name='demo'),
]