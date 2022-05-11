from django.shortcuts import render

# Create your views here.
def default_map(request):
    # TODO: move this token to Django settings from an environment variable
    # found in the Mapbox account settings and getting started instructions
    # see https://www.mapbox.com/account/ under the "Access tokens" section
    mapbox_access_token = 'pk.eyJ1IjoibWh1cHAiLCJhIjoiY2wyN3YzMTRzMDFiZzNrbzhoZXZtcG4yYiJ9.q9cjSjkeABVIX-TIVHeHYA'
    return render(request, 'default.html', 
                  { 'mapbox_access_token': mapbox_access_token })    
            
