from django.shortcuts import render, redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.views import generic
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from .forms import CreateUserForm


def index(request):
    return render(request, 'home/main.html', {})

def registerPage(request):

    if request.user.is_authenticated:

        print(request.user)
        q1 = [1, 0]
        q2 = ["Yes", "No"]
        zip_list = zip(q1, q2)
        zip_list2 = zip(q1, q2)
        zip_list3 = zip(q1, q2)

        return render(request, 'polls/index.html', {"liste": zip_list, "liste2": zip_list2, "liste3": zip_list3})

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
        q1 = [1, 0]
        q2 = ["Yes", "No"]
        zip_list = zip(q1, q2)
        zip_list2 = zip(q1, q2)
        zip_list3 = zip(q1, q2)

        return render(request, 'polls/index.html', {"liste": zip_list, "liste2": zip_list2, "liste3": zip_list3})


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

                return render(request, 'polls/index.html', {"liste": zip_list, "liste2": zip_list2, "liste3": zip_list3})

            else:
                messages.success(request, ("There was a Error login in, Try again"))
                return redirect('login')

        else:
            # Return an 'invalid login' error message.
            return render(request, 'registration/login.html', {})



def logout_user(request):
    logout(request)
    return redirect('login')