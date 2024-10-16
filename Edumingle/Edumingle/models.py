# myapp/models.py
from django.db import models

class quizResult(models.Model):
    studentid = models.DecimalField(max_digits=10, decimal_places=2)
    question = models.CharField(max_length=200)
    answer = models.CharField(max_length=200)