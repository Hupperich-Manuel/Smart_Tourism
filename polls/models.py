from time import time
from django.db import models
import datetime
from django.utils import timezone
from django.contrib.auth.models import AbstractUser


class Question(models.Model):
    pub_date = models.DateTimeField('date published')
    name = models.CharField('Building_name',max_length=200)
    longitud = models.FloatField("Longitud")
    latitud = models.FloatField("Latitud")
    question_text1 = models.IntegerField("Do you like places that service alcohol?")
    question_text2 = models.IntegerField('Do you enjoy trend places?')
    question_text3 = models.IntegerField('Do you enjoy crowded places?')
    def __str__(self):
        return self.name
    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)

# class Choice(models.Model):
#     question = models.ForeignKey(Question, on_delete=models.CASCADE)
#     choice_text = models.CharField(max_length=200)
#     votes = models.IntegerField(default=0)
#     def __str__(self):
#         return self.choice_text

class Customer(models.Model):
    email = models.CharField("Email", primary_key=True, max_length=200)
    pub_date = models.DateTimeField('date published')
    name = models.CharField('Name', max_length=200)
    surname = models.CharField('Surame', max_length=200)
    question_text1 = models.IntegerField("Do you like places that service alcohol?")
    question_text2 = models.IntegerField('Do you enjoy trend places?')
    question_text3 = models.IntegerField('Do you enjoy crowded places?')
    valuation = models.FloatField("Validation",default=0)
    def __str__(self):
        return self.name
