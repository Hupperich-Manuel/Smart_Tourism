from django.shortcuts import render, redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.views import generic
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from .forms import CreateUserForm
from django.http import HttpResponseRedirect
from django.urls import reverse
from polls.models import Customer



def index(request):
    return render(request, 'home/main.html', {})

def registerPage(request):

    if request.user.is_authenticated:

        user_in_date = Customer.objects.get(username_id=request.user)
        if user_in_date is not None:
        
            return HttpResponseRedirect(reverse('polls:second_user', args=()))

        else:
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
                                                    # "liste17": zip_list17,
                                                    # "liste18": zip_list18,
                                                    # "liste19": zip_list19,
                                                    # "liste20": zip_list20
                                                    })

    else:
        form = CreateUserForm()


        if request.method == "POST":
            form = CreateUserForm(request.POST)
            if form.is_valid():
                form.save()
                user = form.cleaned_data.get('username')
                messages.success(request, ("Account was created for "+user))
                return redirect('login')


        context = {"form":form}
        return render(request, 'registration/register.html', context)

def login_user(request):

    if request.user.is_authenticated:

        user_in_date = Customer.objects.get(username_id=request.user)
        if user_in_date is not None:
        
            return HttpResponseRedirect(reverse('polls:second_user', args=()))

        else:
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
                                                    # "liste17": zip_list17,
                                                    # "liste18": zip_list18,
                                                    # "liste19": zip_list19,
                                                    # "liste20": zip_list20
                                                    })


    else:
        if request.method == "POST":
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                # Redirect to a success page.
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
                                                # "liste17": zip_list17,
                                                # "liste18": zip_list18,
                                                # "liste19": zip_list19,
                                                # "liste20": zip_list20
                                                })

            else:
                messages.success(request, ("There was a Error login in, Try again"))
                return redirect('login')

        else:
            # Return an 'invalid login' error message.
            return render(request, 'registration/login.html', {})



def logout_user(request):
    logout(request)
    return redirect('login')