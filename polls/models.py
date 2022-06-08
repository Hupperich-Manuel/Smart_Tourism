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
    question_text1 = models.IntegerField("Do you prefer popular places with a lot of foot traffic over quiet places?")
    question_text2 = models.IntegerField('Do you like to explore popular places?')
    question_text3 = models.IntegerField('Are you willing to spend money on pricey experiences?')
    question_text4 = models.IntegerField('Do you like to explore nature and green spaces when in a new city?')
    question_text5 = models.IntegerField('Is it important to you to go to scenic places with great photo opportunities?')
    question_text6 = models.IntegerField('When travelling are you looking for gambling opportunities (i.e. casinos, race tracks, etc.)')
    question_text7 = models.IntegerField('Do you prefer places with a lot of restaurants around?')
    question_text8 = models.IntegerField('Do you like laid-back and casual spots?')
    question_text9 = models.IntegerField('Do you need publicly available Wifi options during your visit?')
    question_text10 = models.IntegerField('Are you interested in history and historic places?')
    question_text11 = models.IntegerField('Are you a person that likes to visit museums (art, history, curiosities, etc.)?')
    question_text12 = models.IntegerField('Do you enjoy street performances?')
    question_text13 = models.IntegerField('Are you looking for authentic local experiences?')
    question_text14 = models.IntegerField('Do you enjoy sitting outside and taking it easy?')
    question_text15 = models.IntegerField('Do you enjoy crowded places?')
    question_text16 = models.IntegerField('Are you travelling with a romantic partner and want to find a special place to take them to?')
    question_text17 = models.IntegerField('Are you into literature and books?')
    question_text18 = models.IntegerField('Are you a sporty person and looking for sports opportunities while travelling?')
    question_text19 = models.IntegerField('Do you usually travel with your family and look for family-friendly places?')
    question_text20 = models.IntegerField('Do you travel with your pet(s) or like to go to animal-friendly places (i.e. dog parks)?')
    description = models.CharField('Building Description', max_length=1000)
    
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
    question_text1 = models.IntegerField("Do you prefer popular places with a lot of foot traffic over quiet places?")
    question_text2 = models.IntegerField('Do you like to explore popular places?')
    question_text3 = models.IntegerField('Are you willing to spend money on pricey experiences?')
    question_text4 = models.IntegerField('Do you like to explore nature and green spaces when in a new city?')
    question_text5 = models.IntegerField('Is it important to you to go to scenic places with great photo opportunities?')
    question_text6 = models.IntegerField('When travelling are you looking for gambling opportunities (i.e. casinos, race tracks, etc.)')
    question_text7 = models.IntegerField('Do you prefer places with a lot of restaurants around?')
    question_text8 = models.IntegerField('Do you like laid-back and casual spots?')
    question_text9 = models.IntegerField('Do you need publicly available Wifi options during your visit?')
    question_text10 = models.IntegerField('Are you interested in history and historic places?')
    question_text11 = models.IntegerField('Are you a person that likes to visit museums (art, history, curiosities, etc.)?')
    question_text12 = models.IntegerField('Do you enjoy street performances?')
    question_text13 = models.IntegerField('Are you looking for authentic local experiences?')
    question_text14 = models.IntegerField('Do you enjoy sitting outside and taking it easy?')
    question_text15 = models.IntegerField('Do you enjoy crowded places?')
    question_text16 = models.IntegerField('Are you travelling with a romantic partner and want to find a special place to take them to?')
    question_text17 = models.IntegerField('Are you into literature and books?')
    question_text18 = models.IntegerField('Are you a sporty person and looking for sports opportunities while travelling?')
    question_text19 = models.IntegerField('Do you usually travel with your family and look for family-friendly places?')
    question_text20 = models.IntegerField('Do you travel with your pet(s) or like to go to animal-friendly places (i.e. dog parks)?')
    building = models.ForeignKey(Question,unique=False, to_field='building', on_delete=models.CASCADE, default=None)
    dot_product = models.FloatField("Validation_Dot_Product",default=0)
    valuation = models.FloatField("Validation",default=0)
    opinion = models.CharField('Opinion', max_length=1000,default='No Opinion')

