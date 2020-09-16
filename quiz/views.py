from rest_framework.response import Response
from rest_framework import generics, viewsets
from rest_framework.exceptions import(
    ValidationError, PermissionDenied
)
from rest_framework.permissions import IsAuthenticated
from quiz.models import Quiz, Question
from quiz.serializers import QuizSerializer, QuestionSerializer


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


class QuizQuestions(generics.ListCreateAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = QuestionSerializer

    def queryset(self):
        if self.kwargs.get("quiz_pk"):
            quiz = Quiz.objects.get(pk=self.kwargs["quiz_pk"])
            queryset = Question.objects.filter(
                owner= self.request.user,
                quiz=quiz
            )
            return queryset

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class SingleQuizQuestion(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        if self.kwarg.get("quiz_pk") and self.kwargs.get("pk"):
            quiz = Quiz.objects.get(pk=self.kwargs["quiz_pk"])
            queryset = Question.objects.filter(
                pk=self.kwargs["pk"],
                owner=self.request.user,
                quiz=quiz)
            return queryset

class QuestionViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    serializer_class = QuestionSerializer

    def get_queryset(self):
        queryset = Question.objects.all().filter(owner=self.request.user)
        return queryset

    def create(self, request, *args, **kwargs):
        if request.user.is_anonymous:
            raise PermissionDenied(
                "Only logged in users with accounts can create quizzes"
            )

        return super().create(request, *args, **kwargs)

    def destroy(self, request, *args, **kwargs):
        question = Question.objects.get(pk=self.kwargs["pk"])
        if not request.user == question.owner:
            raise PermissionDenied(
                "You have no permissions to edit this question"
            )
        return super().update(request, *args, **kwargs)



