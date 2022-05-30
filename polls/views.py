from string import punctuation
from django.urls import reverse
from urllib import response
from django.shortcuts import get_list_or_404, render, get_object_or_404
from django.views import generic
from .models import Question, Customer
from django.http import HttpResponseRedirect
from django.utils import timezone
import sqlite3
import numpy as np


# class IndexView(generic.ListView):
#     template_name = 'polls/index.html'
#     context_object_name = 'latest_question_list'

#     def get_queryset(self):
#         """Return the last five published questions."""
#         return Question.objects.get('-pub_date')[:5]

def IndexView(request):
    """Return the last five published questions."""
    q1 = [1, 0]
    q2 = ["Yes", "No"]
    zip_list = zip(q1, q2)
    zip_list2 = zip(q1, q2)
    zip_list3 = zip(q1, q2)


    return render(request, 'polls/index.html', {"liste": zip_list, "liste2": zip_list2, "liste3": zip_list3})


def ResultsView(request, place1,lon1, lat1, place2,lon2, lat2,  place3, lon3, lat3):
    print(lat1)
    print(lon1)


    result = [place1, place2, place3]

    coordinates_start = [lon1, lat1, lon2, lat2,lon3, lat3]

    mapbox_access_token = 'pk.eyJ1IjoibWh1cHAiLCJhIjoiY2wyN3YzMTRzMDFiZzNrbzhoZXZtcG4yYiJ9.q9cjSjkeABVIX-TIVHeHYA'
    return render(request, 'polls/map.html', 
                  { 'mapbox_access_token': mapbox_access_token ,
                    "q1": result,
                    "coordinates_start":coordinates_start
                    })


def default_map(request):
    # TODO: move this token to Django settings from an environment variable
    # found in the Mapbox account settings and getting started instructions
    # see https://www.mapbox.com/account/ under the "Access tokens" section
    mapbox_access_token = 'pk.eyJ1IjoibWh1cHAiLCJhIjoiY2wyN3YzMTRzMDFiZzNrbzhoZXZtcG4yYiJ9.q9cjSjkeABVIX-TIVHeHYA'
    return render(request, 'polls/map.html', 
                  { 'mapbox_access_token': mapbox_access_token })

def modelling(request):

    """
    Returns the answers of the votes
    """
    name=request.POST['answer0']
    surname = request.POST['answer01']
    answer1=request.POST['answer1']
    answer2 = request.POST['answer2']
    answer3 = request.POST['answer3']
    email=request.POST['answer4']


    

    try:
        selected_choice = Customer(
                                   email= email,
                                   pub_date=timezone.now(),
                                   name=name,
                                   surname=surname, 
                                   question_text1=answer1, 
                                   question_text2 = answer2,
                                   question_text3 = answer3
                                   )


    except (KeyError, Customer.DoesNotExist):
        q1 = [1, 0]
        q2 = ["Yes", "No"]
        zip_list = zip(q1, q2)
        zip_list2 = zip(q1, q2)
        zip_list3 = zip(q1, q2)
        return render(request, 'polls/index.html',{
            "liste": zip_list, 
            "liste2": zip_list2, 
            "liste3": zip_list3,
            'error_message':'You did not select a choice'})

    else:
        if selected_choice:
            selected_choice.save()

            conn = sqlite3.connect('db.sqlite3')
            cursor = conn.cursor()
            conn.commit()

            print('\nColumns in Customer table')
            data = cursor.execute('''SELECT longitud, latitud, question_text1, question_text2, question_text3 FROM polls_question''')

            places = {}
            for index, column in enumerate(data):
                
                places[index] = [column[0], column[1], np.dot(column[2:], [int(answer1), int(answer2), int(answer3)])]
            


            places = dict(sorted(places.items(), key=lambda x: x[1][2], reverse=True)[:3])

            selected_experience = []
            for key in places.keys():
                selected_experience.append(str(Question.objects.get(pk=key)))
                selected_experience.append(str(places[key][0]))
                selected_experience.append(str(places[key][1]))
                selected_experience




        return HttpResponseRedirect(reverse('polls:results', args=(selected_experience)))




def rating(request):

    place1 = []
    place2 = []
    place3 = []

    for i in range(1, 6):
        place1.append(int(request.POST.get(f'demo{i}', 0)))
        place2.append(int(request.POST.get(f'demo1{i}', 0)))
        place3.append(int(request.POST.get(f'demo2{i}', 0)))


    # if place1 == []:
    #     q1 = [1, 0]
    #     q2 = ["Yes", "No"]
    #     zip_list = zip(q1, q2)
    #     zip_list2 = zip(q1, q2)
    #     zip_list3 = zip(q1, q2)
    #     return render(request, 'polls/index.html',{
    #         "liste": zip_list, 
    #         "liste2": zip_list2, 
    #         "liste3": zip_list3,
    #         'error_message':'no selected places'})

    email=request.POST['email']

    conn = sqlite3.connect('db.sqlite3')
    cursor = conn.cursor()
    conn.commit()

    print('\nColumns in Customer table')
    data = cursor.execute('''SELECT email FROM polls_customer''')

    
    is_in_dataset = False

    for i in data:
        if email != i[0]:
            continue
        else:
            is_in_dataset = True

    if is_in_dataset == False:
        q1 = [1, 0]
        q2 = ["Yes", "No"]
        zip_list = zip(q1, q2)
        zip_list2 = zip(q1, q2)
        zip_list3 = zip(q1, q2)
        return render(request, 'polls/index.html',{
            "liste": zip_list, 
            "liste2": zip_list2, 
            "liste3": zip_list3,
            'error_message':'Not registered email'})


    evaluation = round((max(place1)+max(place2)+max(place3))/3,3)
    print(evaluation)


    rate = Customer.objects.get(pk=email)
    name = Customer.objects.filter(pk=email).values_list('name', flat=True)
    print(name)

    rate.valuation = evaluation

    rate.save()

    feedback = "Neutral"

    if evaluation<=3:
        feedback = "Poor"

    elif 3<evaluation<4.5:
        feedback = "Normal"

    else:
        feedback = "Very Good"


    return render(request, 'polls/answers.html', {"feedback":feedback, "punctuation":evaluation, "name":name[0]})