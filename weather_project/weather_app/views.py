import datetime

import requests
from django.shortcuts import render


# Create your views here.
def index(request):
    API_KEY = open("API_KEY", "r").read()
    current_weather_url = "https://api.openweathermap.org/data/2.5/weather?q={}&appid={}"
    forecast_url = "https://api.openweathermap.org/data/2.5/onecall?lat={}&lon={}&exclude=current, munutely,hourly, alerts&appid={}"
    
    if request.method == "POST":
        city1 = request.POST['city1']
        city2 = request.get('city2', None)
    else:
        return render(request, "weather_app/index.html")