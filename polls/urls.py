from django.urls import path
from . import views

app_name = 'polls'
urlpatterns = [
    path('', views.IndexView, name='index'),
    path('map', views.default_map, name="map"),
    path('<str:place1>/<str:lon1>/<str:lat1>/<str:place2>/<str:lon2>/<str:lat2>/<str:place3>/<str:lon3>/<str:lat3>/results/', views.ResultsView, name='results'),
    path('modelling/', views.modelling, name='modelling'),
    path('rating/', views.rating, name='rating'),
]