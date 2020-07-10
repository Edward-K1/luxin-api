from django.db import models
from django.contrib.auth.models import User


class LuxinUser(User):
    class Meta:
        proxy = True
        ordering = ('first_name', )


class Assessment(models.Model):
    name = models.CharField(max_length=100)


class Question(models.Model):
    assessment = models.ForeignKey(Assessment, on_delete=models.CASCADE)
    text = models.CharField(max_length=200)


class Answer(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    text = models.CharField(max_length=200)


class QuestionAndAnswer(models.Model):
    question = models.OneToOneField(Question, on_delete=models.CASCADE)
    answer = models.OneToOneField(Answer, on_delete=models.CASCADE)
