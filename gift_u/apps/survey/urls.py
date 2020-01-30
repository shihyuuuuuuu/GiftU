from django.urls import path

from .views import (
    QuestionnaireView
)

# Can be used as : "{% url 'survey:index' %}"
app_name = 'survey'

urlpatterns = [
    # ex: /survey/
    path('', QuestionnaireView.as_view(), name='index'),
    # # ex: /survey/5/
    # path('<int:question_id>/', Questionnaire.as_view(), name='detail'),
    # ex: /survey/John/1/
    # path('/<str:creator>/<int:question_id>/', views.index, name='index'),
    # # ex: /survey/5/vote/
    # path('<int:question_id>/vote/', views.vote, name='vote'),
    # Deprecated
    # path('demo', views.demo, name='demo'),
]