from rest_framework import serializers
from apps.quiz.models import Quiz, Question


class QuestionSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    class Meta:
        model = Question
        fields = ('id', 'quiz', 'owner', 'question', 'order', 'choice', 'answer')


class QuizSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')

    #this currently has a problem on the server
    question = QuestionSerializer(many=True, read_only=True, required=False)
    #AssertionError 'The field 'question' was declared on serializer QuizSerializer, but has not been included in the 'fields' option.'



    class Meta:
        model = Quiz
        fields = ('id', 'owner', 'directions', 'name', 'question')






