from datetime import timedelta
from string import punctuation
from django.urls import reverse
from urllib import response
from django.shortcuts import get_list_or_404, render, get_object_or_404
from django.views import generic
from .models import Question, Customer, User
from django.http import HttpResponseRedirect
from django.utils import timezone
import psycopg2
import numpy as np
import os
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.shortcuts import render, redirect





# class IndexView(generic.ListView):
#     template_name = 'polls/index.html'
#     context_object_name = 'latest_question_list'

#     def get_queryset(self):
#         """Return the last five published questions."""
#         return Question.objects.get('-pub_date')[:5]

@login_required(login_url='login')
def IndexView(request):
    """Return the last five published questions."""
    q1 = [1, 0]
    q2 = ["Yes", "No"]
    zip_list = zip(q1, q2)
    zip_list2 = zip(q1, q2)
    zip_list3 = zip(q1, q2)
    zip_list4 = zip(q1, q2)
    zip_list5 = zip(q1, q2)
    zip_list6 = zip(q1, q2)
    zip_list7 = zip(q1, q2)
    zip_list8 = zip(q1, q2)
    zip_list9 = zip(q1, q2)
    zip_list10 = zip(q1, q2)
    zip_list11 = zip(q1, q2)
    zip_list12 = zip(q1, q2)
    zip_list13 = zip(q1, q2)
    zip_list14 = zip(q1, q2)
    zip_list15 = zip(q1, q2)
    zip_list16 = zip(q1, q2)
    zip_list17 = zip(q1, q2)
    zip_list18 = zip(q1, q2)
    zip_list19 = zip(q1, q2)
    zip_list20 = zip(q1, q2)

    return render(request, 'polls/index.html', {"liste": zip_list, 
                                                "liste2": zip_list2, 
                                                "liste3": zip_list3,
                                                "liste4": zip_list4,
                                                "liste5": zip_list5,
                                                "liste6": zip_list6,
                                                "liste7": zip_list7,
                                                "liste8": zip_list8,
                                                "liste9": zip_list9,
                                                "liste10": zip_list10,
                                                "liste11": zip_list11,
                                                "liste12": zip_list12,
                                                "liste13": zip_list13,
                                                "liste14": zip_list14,
                                                "liste15": zip_list15,
                                                "liste16": zip_list16,
                                                "liste17": zip_list17,
                                                "liste18": zip_list18,
                                                "liste19": zip_list19,
                                                "liste20": zip_list20
                                                })

@login_required(login_url='login')
def ResultsView(request, place1,lon1, lat1, place2,lon2, lat2,  place3, lon3, lat3, place4, lon4, lat4, place5, lon5, lat5):
    


    result = [place1, place2, place3, place4, place5]

    coordinates_start = [lon1, lat1, lon2, lat2,lon3, lat3,lon4, lat4,lon5, lat5]

    mapbox_access_token = 'mapbox_access_token'
    return render(request, 'polls/map.html', 
                { 'mapbox_access_token': 'pk.eyJ1IjoibWh1cHAiLCJhIjoiY2wyN3YzMTRzMDFiZzNrbzhoZXZtcG4yYiJ9.q9cjSjkeABVIX-TIVHeHYA' ,
                    "q1": result,
                    "coordinates_start":coordinates_start
                    })

@login_required(login_url='login')
def default_map(request):
    # TODO: move this token to Django settings from an environment variable
    # found in the Mapbox account settings and getting started instructions
    # see https://www.mapbox.com/account/ under the "Access tokens" section
    mapbox_access_token = 'pk.eyJ1IjoibWh1cHAiLCJhIjoiY2wyN3YzMTRzMDFiZzNrbzhoZXZtcG4yYiJ9.q9cjSjkeABVIX-TIVHeHYA'
    return render(request, 'polls/map.html', 
                  { 'mapbox_access_token': mapbox_access_token })

@login_required(login_url='login')
def modelling(request):

    """
    Returns the answers of the votes
    """


    try:

        answer1=request.POST['answer1']
        answer2 = request.POST['answer2']
        answer3 = request.POST['answer3']
        answer4=request.POST['answer4']
        answer5 = request.POST['answer5']
        answer6 = request.POST['answer6']
        answer7=request.POST['answer7']
        answer8 = request.POST['answer8']
        answer9 = request.POST['answer9']
        answer10=request.POST['answer10']
        answer11 = request.POST['answer11']
        answer12 = request.POST['answer12']
        answer13=request.POST['answer13']
        answer14 = request.POST['answer14']
        answer15 = request.POST['answer15']
        answer16 = request.POST['answer16']
        answer17 = request.POST['answer17']
        answer18 = request.POST['answer18']
        answer19 = request.POST['answer19']
        answer20 = request.POST['answer20']

        print(answer3)

    except (KeyError, Customer.DoesNotExist):
        q1 = [1, 0]
        q2 = ["Yes", "No"]
        zip_list = zip(q1, q2)
        zip_list2 = zip(q1, q2)
        zip_list3 = zip(q1, q2)
        zip_list4 = zip(q1, q2)
        zip_list5 = zip(q1, q2)
        zip_list6 = zip(q1, q2)
        zip_list7 = zip(q1, q2)
        zip_list8 = zip(q1, q2)
        zip_list9 = zip(q1, q2)
        zip_list10 = zip(q1, q2)
        zip_list11 = zip(q1, q2)
        zip_list12 = zip(q1, q2)
        zip_list13 = zip(q1, q2)
        zip_list14 = zip(q1, q2)
        zip_list15 = zip(q1, q2)
        zip_list16 = zip(q1, q2)
        zip_list17 = zip(q1, q2)
        zip_list18 = zip(q1, q2)
        zip_list19 = zip(q1, q2)
        zip_list20 = zip(q1, q2)
        return render(request, 'polls/index.html',{"liste": zip_list, 
                                                "liste2": zip_list2, 
                                                "liste3": zip_list3,
                                                "liste4": zip_list4,
                                                "liste5": zip_list5,
                                                "liste6": zip_list6,
                                                "liste7": zip_list7,
                                                "liste8": zip_list8,
                                                "liste9": zip_list9,
                                                "liste10": zip_list10,
                                                "liste11": zip_list11,
                                                "liste12": zip_list12,
                                                "liste13": zip_list13,
                                                "liste14": zip_list14,
                                                "liste15": zip_list15,
                                                "liste16": zip_list16,
                                                "liste17": zip_list17,
                                                "liste18": zip_list18,
                                                "liste19": zip_list19,
                                                "liste20": zip_list20,
                                                'error_message':'You did not select a choice'})


    if (answer1 != None)&(answer2 != None)&(answer3 != None)&(answer4 != None)&(answer5 != None)&(answer6 != None)&(answer7 != None)&(answer8 != None)&(answer9 != None)&(answer10 != None)&(answer11 != None)&(answer12 != None)&(answer13 != None)&(answer14 != None)&(answer15 != None)&(answer16 != None)&(answer17 != None)&(answer18 != None)&(answer19 != None)&(answer20 != None):

        conn = psycopg2.connect(user='lhmbwwvwzdowlh',
                                password='612b019afb4141573c0975be3c49699c457cae4ec77d2bb5565cec32605b42f0',
                                host="ec2-52-44-13-158.compute-1.amazonaws.com",
                                port="5432",
                                database="d3uubo8qgsm2jg")

        # conn = psycopg2.connect(user='postgres',
        #                         password='shandy123',
        #                         host="127.0.0.1",
        #                         port="5432",
        #                         database="new")
        cursor = conn.cursor()      
        #conn.commit()

        print('\nColumns in Customer table')
        cursor.execute('''SELECT * FROM polls_question''')
        data = cursor.fetchall()


        print(data)
        places = {}
        dot_product_answer = [int(answer1), int(answer2), int(answer3), int(answer4), int(answer5), int(answer6), int(answer7),
                              int(answer8), int(answer9), int(answer10), int(answer11), int(answer12), int(answer13), int(answer14),
                              int(answer15), int(answer16), int(answer17), int(answer18), int(answer19), int(answer20)]
        
        for index, column in enumerate(data):

            print(column)
            
            places[index] = [column[0], column[1],column[2], np.dot(list(column[3:]), dot_product_answer)]
        
        places = dict(sorted(places.items(), key=lambda x: x[1][3], reverse=True)[:5])


        selected_experience = []
        for key in places.keys():
            selected_experience.append(str(Question.objects.get(pk=places[key][0])))
            selected_experience.append(str(places[key][1]))
            selected_experience.append(str(places[key][2]))

        select_place = []
        for index, building in enumerate(selected_experience):

             if index%3 == 0:

                selected_choice = Customer(username_id=User.objects.get(username=request.user),
                                    email= request.user.email,
                                    pub_date=timezone.now(),
                                    name=request.user.first_name,
                                    surname=request.user.last_name, 
                                    question_text1=answer1, 
                                    question_text2 = answer2,
                                    question_text3 = answer3,
                                    question_text4 = answer4,
                                    question_text5 = answer5,
                                    question_text6 = answer6,
                                    question_text7 = answer7,
                                    question_text8 = answer8,
                                    question_text9 = answer9,
                                    question_text10 = answer10,
                                    question_text11 = answer11,
                                    question_text12 = answer12,
                                    question_text13 = answer13,
                                    question_text14 = answer14,
                                    question_text15 = answer15,
                                    question_text16 = answer16,
                                    question_text17 = answer17,
                                    question_text18 = answer18,
                                    question_text19 = answer19,
                                    question_text20 = answer20,
                                    building_id = Question.objects.get(building=selected_experience[index])
                                    )
                select_place.append(selected_choice)

  

        Customer.objects.bulk_create(select_place)

        print(select_place)
        return HttpResponseRedirect(reverse('polls:results', args=(selected_experience)))


    else:

        messages.success(request, ("There was a Error submitting your responses (You must answer all questions), Try again"))

        q1 = [1, 0]
        q2 = ["Yes", "No"]
        zip_list = zip(q1, q2)
        zip_list2 = zip(q1, q2)
        zip_list3 = zip(q1, q2)
        zip_list4 = zip(q1, q2)
        zip_list5 = zip(q1, q2)
        zip_list6 = zip(q1, q2)
        zip_list7 = zip(q1, q2)
        zip_list8 = zip(q1, q2)
        zip_list9 = zip(q1, q2)
        zip_list10 = zip(q1, q2)
        zip_list11 = zip(q1, q2)
        zip_list12 = zip(q1, q2)
        zip_list13 = zip(q1, q2)
        zip_list14 = zip(q1, q2)
        zip_list15 = zip(q1, q2)
        zip_list16 = zip(q1, q2)
        zip_list17 = zip(q1, q2)
        zip_list18 = zip(q1, q2)
        zip_list19 = zip(q1, q2)
        zip_list20 = zip(q1, q2)
        return HttpResponseRedirect(reverse('polls:index'))





    



@login_required(login_url='login')
def rating(request, building1, building2, building3, building4, building5):


    try:

        place1 = int(request.POST.get(f'demo', 0))
        place2 = int(request.POST.get(f'demo1', 0))
        place3 = int(request.POST.get(f'demo2', 0))
        place4 = int(request.POST.get(f'demo3', 0))
        place5 = int(request.POST.get(f'demo4', 0))
    
        opinions = request.POST.get('comments',None)


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

        username = request.user
    except (KeyError, Customer.DoesNotExist):

        messages.success(request, ("There was a Error submitting your responses (You must answer all questions), Try again"))

        q1 = [1, 0]
        q2 = ["Yes", "No"]
        zip_list = zip(q1, q2)
        zip_list2 = zip(q1, q2)
        zip_list3 = zip(q1, q2)
        zip_list4 = zip(q1, q2)
        zip_list5 = zip(q1, q2)
        zip_list6 = zip(q1, q2)
        zip_list7 = zip(q1, q2)
        zip_list8 = zip(q1, q2)
        zip_list9 = zip(q1, q2)
        zip_list10 = zip(q1, q2)
        zip_list11 = zip(q1, q2)
        zip_list12 = zip(q1, q2)
        zip_list13 = zip(q1, q2)
        zip_list14 = zip(q1, q2)
        zip_list15 = zip(q1, q2)
        zip_list16 = zip(q1, q2)
        zip_list17 = zip(q1, q2)
        zip_list18 = zip(q1, q2)
        zip_list19 = zip(q1, q2)
        zip_list20 = zip(q1, q2)
        return render(request, 'polls/index.html',{"liste": zip_list, 
                                                "liste2": zip_list2, 
                                                "liste3": zip_list3,
                                                "liste4": zip_list4,
                                                "liste5": zip_list5,
                                                "liste6": zip_list6,
                                                "liste7": zip_list7,
                                                "liste8": zip_list8,
                                                "liste9": zip_list9,
                                                "liste10": zip_list10,
                                                "liste11": zip_list11,
                                                "liste12": zip_list12,
                                                "liste13": zip_list13,
                                                "liste14": zip_list14,
                                                "liste15": zip_list15,
                                                "liste16": zip_list16,
                                                "liste17": zip_list17,
                                                "liste18": zip_list18,
                                                "liste19": zip_list19,
                                                "liste20": zip_list20,
                                                'error_message':'You did not select a choice'})

    #conn = sqlite3.connect('db.sqlite3', timeout=40)
    #cursor = conn.cursor()
    #conn.commit()

    #print('\nColumns in Customer table')
    #data = cursor.execute('''SELECT username_id FROM polls_customer''')

    
    #is_in_dataset = False

    # for i in data:
    #     if username != i[-1]:
    #         print(i[-1])
    #         continue
    #     else:
    #      is_in_dataset = True

    # if is_in_dataset == False:

    #       print("is in dataset is false")
    #       q1 = [1, 0]
    #       q2 = ["Yes", "No"]
    #       zip_list = zip(q1, q2)
    #       zip_list2 = zip(q1, q2)
    #       zip_list3 = zip(q1, q2)
    #       return render(request, 'polls/index.html',{
    #           "liste": zip_list, 
    #           "liste2": zip_list2, 
    #           "liste3": zip_list3,
    #           'error_message':'Not registered email'})

    print(place1)

    print(place2)

    print(place3)

    evaluation = round(((place1+place2+place3+place4+place5)/5),3)


    name = Customer.objects.filter(username_id=username).values_list('name', flat=True)
    
    print(building3)
    for build, val in zip([building1, building2, building3, building4, building5], [place1,place2,place3, place4, place5]):
        
        #rate = Customer.objects.get(building_id=build, username_id=username, pub_date=timezone.now().minute-timedelta(minutes=10))
        rate = Customer.objects.filter(building_id=build, username_id=username).last()
        
        #for index, rt in enumerate()
        print(f"rate: {rate}")

        rate.valuation = val
        rate.opinion = opinions

        rate.save()
        #break

    feedback = "Neutral"

    if evaluation<=3:
        feedback = "Poor"

    elif 3<evaluation<4.5:
        feedback = "Normal"

    else:
        feedback = "Very Good"


    return render(request, 'polls/answers.html', {"feedback":feedback, "punctuation":evaluation, "name":name[0]})