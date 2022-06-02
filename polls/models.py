from time import time
from django.db import models
import datetime
from django.utils import timezone
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import User




class Question(models.Model):
    building = models.CharField('Building_name',unique=True,primary_key=True, max_length=200)
    longitud = models.FloatField("Longitud")
    latitud = models.FloatField("Latitud")
    question_text1 = models.IntegerField("Do you like places that service alcohol?")
    question_text2 = models.IntegerField('Do you enjoy trend places?')
    question_text3 = models.IntegerField('Do you enjoy crowded places?')
    def __str__(self):
        return self.building


# class Choice(models.Model):
#     question = models.ForeignKey(Question, on_delete=models.CASCADE)
#     choice_text = models.CharField(max_length=200)
#     votes = models.IntegerField(default=0)
#     def __str__(self):
#         return self.choice_text

class Customer(models.Model):
    username = models.ForeignKey(User,unique=False, to_field='username', on_delete=models.CASCADE)
    email = models.CharField("Email", max_length=200)
    pub_date = models.DateTimeField('date published')
    name = models.CharField('Name', max_length=200)
    surname = models.CharField('Surame', max_length=200)
    question_text1 = models.IntegerField("Do you like places that service alcohol?")
    question_text2 = models.IntegerField('Do you enjoy trend places?')
    question_text3 = models.IntegerField('Do you enjoy crowded places?')
    building = models.ForeignKey(Question,unique=False, to_field='building', on_delete=models.CASCADE, default=None)
    valuation = models.FloatField("Validation",default=0)
    def __str__(self):
        return self.name
