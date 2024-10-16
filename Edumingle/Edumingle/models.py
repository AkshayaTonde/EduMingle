# myapp/models.py
from django.db import models

class quizResult(models.Model):
    studentid = models.DecimalField(max_digits=10, decimal_places=2)
    question = models.CharField(max_length=200)
    answer = models.CharField(max_length=200)


class quizQuestion(models.Model):
    question = models.CharField(max_length=200)
    option1 = models.CharField(max_length=200)
    option2 = models.CharField(max_length=200)
    option3 = models.CharField(max_length=200)
    option4 = models.CharField(max_length=200)