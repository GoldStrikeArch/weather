import requests
from django.shortcuts import render


def index(request):
    url = 'http://api.openweathermap.org/data/2.5/weather?q={}&units=metric&appid=31eee13d4cd8361b78a94b0fd5cf9ff5'
    city = 'Moscow'

    #Response in json format
    response = requests.get(url.format(city)).json()

    #Dictionary, that represents the data
    city_weather = {
        'city' : city,
        'temperature': response['main']['temp'],
        'description': response['weather'][0]['description'],
        'icon': response['weather'][0]['icon'],

    }
    context = {'city_weather' : city_weather}


    return render(request, 'weather/weather.html', context)
