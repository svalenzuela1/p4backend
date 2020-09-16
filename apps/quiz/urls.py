from django.urls import path, include
from rest_framework import routers
from apps.quiz.views import QuizViewSet, QuizQuestions, SingleQuizQuestion, QuestionViewSet
from django.conf.urls import url

router = routers.DefaultRouter()
router.register('quizzes', QuizViewSet, basename='quizzes')
router.register('questions', QuestionViewSet, basename='questions')

custom_urlpatterns = [
    url(r'quizzes/(?P<quiz_pk>\d+)/questions$', QuizQuestions.as_view(), name='quiz_questions'),
    url(r'quizzes/(?P<quiz_pk>\d+)/questions/(?P<pk>\d+)$', SingleQuizQuestion.as_view(), name='single_quiz_question'),
]

urlpatterns = router.urls
urlpatterns += custom_urlpatterns