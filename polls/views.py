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
from django.contrib.auth.decorators import login_required



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


    return render(request, 'polls/index.html', {"liste": zip_list, "liste2": zip_list2, "liste3": zip_list3})

@login_required(login_url='login')
def ResultsView(request, place1,lon1, lat1, place2,lon2, lat2,  place3, lon3, lat3):
    


    result = [place1, place2, place3]

    coordinates_start = [lon1, lat1, lon2, lat2,lon3, lat3]

    mapbox_access_token = 'mapbox_access_token'
    return render(request, 'polls/map.html', 
                { 'mapbox_access_token': mapbox_access_token ,
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

        print(answer3)

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


    if (answer1 != None)&(answer2 != None)&(answer3 != None):

        conn = psycopg2.connect(user='ecxcznqqewkgel',
                                password='f5666c3d29bb4f435caf7b7b2ab936db75ba8949ed7ad4a212eb479f04ecab25',
                                host="ec2-34-227-120-79.compute-1.amazonaws.com",
                                port="5432",
                                database="dav3cfrln85a50")
        cursor = conn.cursor()      
        #conn.commit()

        print('\nColumns in Customer table')
        cursor.execute('''SELECT building, longitud, latitud, question_text1, question_text2, question_text3 FROM polls_question''')
        data = cursor.fetchall()


        print(data)
        places = {}
        
        for index, column in enumerate(data):
            
            places[index] = [column[0], column[1],column[2], np.dot(list(column[3:]), [int(answer1), int(answer2), int(answer3)])]
        
        places = dict(sorted(places.items(), key=lambda x: x[1][3], reverse=True)[:3])


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
                                    building_id = Question.objects.get(building=selected_experience[index])
                                    )
                select_place.append(selected_choice)
  

        Customer.objects.bulk_create(select_place)



        

        return HttpResponseRedirect(reverse('polls:results', args=(selected_experience)))
    else:

        q1 = [1, 0]
        q2 = ["Yes", "No"]
        zip_list = zip(q1, q2)
        zip_list2 = zip(q1, q2)
        zip_list3 = zip(q1, q2)
        return HttpResponseRedirect(reverse('polls:index'))





    



@login_required(login_url='login')
def rating(request, building1, building2, building3):


    try:

        place1 = int(request.POST.get(f'demo', 0))
        place2 = int(request.POST.get(f'demo1', 0))
        place3 = int(request.POST.get(f'demo2', 0))


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

    evaluation = round(((place1+place2+place3)/3),3)


    name = Customer.objects.filter(username_id=username).values_list('name', flat=True)
    
    print(building3)
    for build, val in zip([building1, building2, building3], [place1,place2,place3]):
        
        rate = Customer.objects.get(building_id=build, username_id=username)
        
        print(f"rate: {rate}")

        rate.valuation = val

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