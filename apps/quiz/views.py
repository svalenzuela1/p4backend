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
class QuizViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    serializer_class = QuizSerializer

    def get_queryset(self):
        queryset = Quiz.objects.all().filter(owner=self.request.user)
        return queryset

    def create(self, request, *args, **kwargs):
        quiz = Quiz.objects.filter(
            name=request.data.get('name'),
            owner=request.user
        )

        if quiz:
            msg = 'Quiz with that name already exists'
            raise ValidationError(msg)
        return super().create(request)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

    def destroy(self, request, *args, **kwargs):
        quiz = Quiz.objects.get(pk=self.kwargs["pk"])
        if not request.user == quiz.owner:
            raise PermissionDenied("You cannot delete this quiz")

        return Response({
            super().destroy(request, *args, **kwargs)
        })





