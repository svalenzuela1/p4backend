from django.db import models
from apps.authentication.models import User


# Create your models here.
class Quiz(models.Model):

    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    description = models.TextField(blank=True)
    question = models.CharField(max_length=100)
    answer = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Question(models.Model):
    class Meta:
        verbose_name_plural = 'questions'

    quiz = models.ForeignKey(Quiz, related_name='questions')
    question = models.CharField(max_length=100)
    #description = models.CharField(max_length=100) <- Should I involve this even though I have questions above
    order = models.IntegerField(default=0)
    choices = models.CharField(max_length=100)
    answer = models.CharField(max_length=100)

class Answer(models.Model):
    class Meta:
        verbose_name_plural = 'answers'

    question = models.ForeignKey(Question, related_name='answers', on_delete=models.CASCADE)
    description = models.CharField(max_length=100)
    is_correct = models.BooleanField(default=False)

    def __str__(self):
        return self.is_correct