import requests
from django.shortcuts import render
from .models import City
from .forms import CityForm

def index(request):
    #You need to get your own appid from openweathermap.org
    url = 'http://api.openweathermap.org/data/2.5/weather?q={}&units=metric&appid=31eee13d4cd8361b78a94b0fd5cf9ff5'
    if request.method == 'POST':
        form = CityForm(request.POST)
        form.save()

    form = CityForm()

    cities = City.objects.all()

    weather_data = []

    #Looping for each city
    for city in cities:
        # Response in json format
        response = requests.get(url.format(city)).json()

        # Dictionary, that represents the data
        city_weather = {
            'city': city.name,
            'temperature': response['main']['temp'],
            'description': response['weather'][0]['description'],
            'icon': response['weather'][0]['icon'],

        }

        weather_data.append(city_weather)
    print(weather_data)

    context = {'weather_data' : weather_data, 'form': form}

    return render(request, 'weather/weather.html', context)
