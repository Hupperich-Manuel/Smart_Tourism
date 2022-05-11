#Spceificy the url for the API methods

from django.conf.urls import url
from EmployeeApp import views

urlpatterns = [
    url(r'', views.index, name='index.html'),
    url(r'^department$', views.departmentApi),
    url(r'^department/([0-9]+)$', views.departmentApi)

]