from django.db import models
from authentication.models import User
#from django.core.validators import MaxValueValidator, MinValueValidator


# Create your models here.
class Quiz(models.Model):
    class Meta:
        verbose_name_plural = 'quizzes'

    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    directions = models.CharField(max_length=250)
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Question(models.Model):

    quiz = models.ForeignKey(Quiz, related_name='questions', on_delete=models.CASCADE)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    question = models.CharField(max_length=100)
    order = models.IntegerField(default=0)
    choice = models.IntegerField(default=4)
    answer = models.CharField(max_length=100)

    def __str__(self):
        return self.answer


# class Answer(models.Model):
#     class Meta:
#         verbose_name_plural = 'answers'
#
#     question = models.ForeignKey(Question, related_name='answers', on_delete=models.CASCADE)
#     answer = models.CharField(max_length=100)
#     is_correct = models.BooleanField(default=False)
#
#
#     def __str__(self):
#         return self.answer