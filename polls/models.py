from time import time
from django.db import models
import datetime
from django.utils import timezone
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import User
#from pyrsistent import v




class Question(models.Model):
    building = models.CharField('Building_name',unique=True,primary_key=True, max_length=200)
    longitud = models.FloatField("Longitud")
    latitud = models.FloatField("Latitud")
    question_text1 = models.IntegerField("Do you prefer popular places with a lot of foot traffic over quiet places?")
    question_text2 = models.IntegerField('Do you like to explore popular places?')
    question_text3 = models.IntegerField('Are you willing to spend money on pricey experiences?')
    question_text4 = models.IntegerField('Do you like to explore nature and green spaces when in a new city?')
    question_text5 = models.IntegerField('Is it important to you to go to scenic places with great photo opportunities?')
    question_text6 = models.IntegerField('Do you travel with your pet(s) or like to go to animal-friendly places (i.e. dog parks)?')
    question_text7 = models.IntegerField('Are you into literature and books?')
    question_text8 = models.IntegerField('Do you like laid-back and casual spots?')
    question_text9 = models.IntegerField('Do you need publicly available Wifi options during your visit?')
    question_text10 = models.IntegerField('Are you interested in history and historic places?')
    question_text11 = models.IntegerField('Are you a person that likes to visit museums (art, history, curiosities, etc.)?')
    question_text12 = models.IntegerField('Do you enjoy street performances?')
    question_text13 = models.IntegerField('Are you looking for authentic local experiences?')
    question_text14 = models.IntegerField('Are you a sporty person and looking for sports opportunities while travelling?')
    question_text15 = models.IntegerField('Do you usually travel with your family and look for family-friendly places?')
    question_text16 = models.IntegerField('Are you travelling with a romantic partner and want to find a special place to take them to?')
    description = models.CharField('Building Description', max_length=1000)
    link = models.CharField('Link to the place', max_length=1000)
    
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
    question_text6 = models.IntegerField('Do you travel with your pet(s) or like to go to animal-friendly places (i.e. dog parks)?')
    question_text7 = models.IntegerField('Are you into literature and books?')
    question_text8 = models.IntegerField('Do you like laid-back and casual spots?')
    question_text9 = models.IntegerField('Do you need publicly available Wifi options during your visit?')
    question_text10 = models.IntegerField('Are you interested in history and historic places?')
    question_text11 = models.IntegerField('Are you a person that likes to visit museums (art, history, curiosities, etc.)?')
    question_text12 = models.IntegerField('Do you enjoy street performances?')
    question_text13 = models.IntegerField('Are you looking for authentic local experiences?')
    question_text14 = models.IntegerField('Are you a sporty person and looking for sports opportunities while travelling?')
    question_text15 = models.IntegerField('Do you usually travel with your family and look for family-friendly places?')
    question_text16 = models.IntegerField('Are you travelling with a romantic partner and want to find a special place to take them to?')
    building = models.ForeignKey(Question,unique=False, to_field='building', on_delete=models.CASCADE, default=None)
    click_on_link = models.IntegerField("If the user clicked on the link or not", default=0)
    dot_product = models.FloatField("Validation_Dot_Product",default=0)
    valuation = models.FloatField("Validation",default=0)
    opinion = models.CharField('Opinion', max_length=1000,default='No Opinion')




class SecondUse(models.Model):
    username = models.ForeignKey(User,unique=False, to_field='username', on_delete=models.CASCADE)
    email = models.CharField("Email", max_length=200)
    pub_date = models.DateTimeField('date published')
    name = models.CharField('Name', max_length=200)
    surname = models.CharField('Surame', max_length=200)
    building = models.ForeignKey(Question,unique=False, to_field='building', on_delete=models.CASCADE, default=None)
    click_on_link = models.IntegerField("If the user clicked on the link or not", default=0)
    dot_product = models.FloatField("Validation_Dot_Product",default=0)
    valuation = models.FloatField("Validation",default=0)
    opinion = models.CharField('Opinion', max_length=1000,default='No Opinion')



class XMatrix(models.Model):
    username = models.CharField('username',  max_length=200,unique=False, primary_key=True)
    bulding_1 = models.IntegerField(default=0)
    bulding_2 = models.IntegerField(default=0)
    bulding_3 = models.IntegerField(default=0)
    bulding_4 = models.IntegerField(default=0)
    bulding_5 = models.IntegerField(default=0)
    bulding_6 = models.IntegerField(default=0)
    bulding_7 = models.IntegerField(default=0)
    bulding_8 = models.IntegerField(default=0)
    bulding_9 = models.IntegerField(default=0)
    bulding_10 = models.IntegerField(default=0)
    bulding_11 = models.IntegerField(default=0)
    bulding_12 = models.IntegerField(default=0)
    bulding_13 = models.IntegerField(default=0)
    bulding_14 = models.IntegerField(default=0)
    bulding_15 = models.IntegerField(default=0)
    bulding_16 = models.IntegerField(default=0)
    bulding_17 = models.IntegerField(default=0)
    bulding_18 = models.IntegerField(default=0)
    bulding_19 = models.IntegerField(default=0)
    bulding_20 = models.IntegerField(default=0)
    bulding_21 = models.IntegerField(default=0)
    bulding_22 = models.IntegerField(default=0)
    bulding_23 = models.IntegerField(default=0)
    bulding_24 = models.IntegerField(default=0)
    bulding_25 = models.IntegerField(default=0)
