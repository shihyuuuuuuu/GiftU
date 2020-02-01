from django.urls import path

from .views import (
    QuestionnaireView
)

# Can be used as : "{% url 'survey:index' %}"
app_name = 'survey'

urlpatterns = [
    # ex: /survey/
    path('', QuestionnaireView.as_view(), name='index'),
    # ex: /survey/2
    path('<str:questionnaire_id>/', QuestionnaireView.as_view(), name='index'),
    # # ex: /survey/5/vote/
    # path('<int:question_id>/vote/', views.vote, name='vote'),
    # Deprecated
    # path('demo', views.demo, name='demo'),
]