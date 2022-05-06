from django.db import models

# Create your models here.
class Quiz(models.Model):
    title = models.CharFiled(max_length=200)
    body = models.TextField()
    answer = models.IntegerField()
    