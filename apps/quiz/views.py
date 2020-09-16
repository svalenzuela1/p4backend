from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import generics, viewsets, status
from rest_framework.exceptions import(
    ValidationError, PermissionDenied
)
from rest_framework.permissions import IsAuthenticated, AllowAny
from apps.quiz.models import Quiz, Question
from apps.quiz.serializers import QuizSerializer, QuestionSerializer


# Create your views here.






