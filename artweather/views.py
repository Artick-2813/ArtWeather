from django.shortcuts import render, redirect
from .models import City
from .forms import CityForm
import requests
from django.views.generic import DeleteView
from django.http import HttpResponse


def index(request):
    api_id = '976fd03c1443765b186f2424b2d61a7d'

    url = 'https://api.openweathermap.org/data/2.5/weather?q={}&units=metric&appid=' + api_id

    if(request.method == 'POST'):
        form = CityForm(request.POST)
        form.save()

    form = CityForm()

    cities = City.objects.all()

    all_cities = []

    for city in cities:

        res = requests.get(url.format(city.name_city)).json()
        if res.get('main'):
            city_info = {
                'city': city.name_city,
                'temp': res['main']['temp'],
                'icon': res['weather'][0]['icon'],
                'error': False,
            }
        else:
            city_info = {
                'city': city.name_city,
                'error': True,
            }

        all_cities.append(city_info)

    context = {'all_info': all_cities, 'form': form}

    return render(request, 'artweather/index.html', context)


def app(request):
    return render(request, 'artweather/application.html')


def delete(request):
    City.objects.all().delete()
    return render(request, 'artweather/delete.html')


