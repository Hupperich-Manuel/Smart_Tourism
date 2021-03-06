from django.urls import path
from . import views

app_name = 'polls'
urlpatterns = [
    path('', views.IndexView, name='index'),
    path('map', views.default_map, name="map"),
    path('second_user', views.SecondUser, name='second_user'),
    path('<str:place1>/<str:lon1>/<str:lat1>/<str:place2>/<str:lon2>/<str:lat2>/<str:place3>/<str:lon3>/<str:lat3>/<str:place4>/<str:lon4>/<str:lat4>/<str:place5>/<str:lon5>/<str:lat5>/results/', views.ResultsView, name='results'),
    path('modelling/', views.modelling, name='modelling'),
    path('<str:building1>/<str:building2>/<str:building3>/<str:building4>/<str:building5>/rating/', views.rating, name='rating'),
    path('<str:building1>/<str:building2>/<str:building3>/<str:building4>/<str:building5>/rating_second/', views.rating_second, name='rating_second'),
]