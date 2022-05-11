from django.shortcuts import render
#We can now start to write the API methods
from django.views.decorators.csrf import csrf_exempt
#from sympy import re
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse

from EmployeeApp.models import Departments, Employees
from EmployeeApp.serializers import DepartmentSerializer, EmployeeSerializer

from django.http import HttpResponse
# Create your views here.

def index(request):
    context = {'a':'HelloWorld!'}
    return render(request, 'index.html', context)

#@csrf_exempt
def departmentApi(request):
    if request.method=="GET":
        departments = Departments.objects.all()
        departments_serializer = DepartmentSerializer(departments, many=True)
        return render(request, 'index.html', departments)

    elif request.method == "POST":
        temp = {}
        dep = request.POST.get('DepartmentId')
        departments_serializer = Departments(DepartmentId=dep, DepartmentName="Manu")
        # department_data =JSONParser().parse(request)
        # departments_serializer = DepartmentSerializer(data=department_data)
        departments_serializer.save()
        dep_serializers = departments_serializer.objects
        contexts = {"posts":"manuel"}
        return render(request, 'index.html', contexts)

    elif request.method=="PUT":
        department_data = JSONParser().parse(request)
        department = Departments.objects.get(DepartmentId=department_data["DepartmentId"])
        departments_serializer = DepartmentSerializer(department, data = department_data)
        if departments_serializer.is_valid():
            departments_serializer.save()
            return JsonResponse("Update Successfully", safe=False)
        return JsonResponse("Failed to Update")

    elif request.method=="DELETE":
        department=Departments.objects.get(Departments=id)
        department.delete()
        return JsonResponse("Deleted Successfully", safe=False)

