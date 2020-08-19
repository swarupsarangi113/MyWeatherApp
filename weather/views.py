from django.shortcuts import render
from .models import City
from .forms import AddCityForm
from django.contrib import messages
import requests,pprint

def home(request) :

    city_weather_list = []

    url = 'http://api.openweathermap.org/data/2.5/weather?q={}&units=metric&APPID=6416aac48188600bd09a4eeecbce5bbd'

    if request.method == 'POST' :
        form = AddCityForm(request.POST)

        if form.is_valid() :
            data = form.cleaned_data.get('city_name')
            res = requests.get(url.format(data))

            city_count = City.objects.filter(city_name=data).count()

            if res.status_code != 404 and city_count == 0 :
                form.save()
                messages.success(request,f'{data} Added !')
            elif city_count > 0 :
                messages.warning(request,f'{data} already present !')
            else :
                messages.warning(request,'Please try again !')
    
    form = AddCityForm()

    cities = City.objects.all().order_by('-date_posted')

    for city in cities :

        res = requests.get(url.format(city.city_name))

        data = res.json()

        city_weather = {
            'city' : city.city_name,
            'country' : data['sys']['country'],
            'temperature': data['main']['temp'],
            'description' : data['weather'][0]['description'],
            'icon' : data['weather'][0]['icon']        
        }

        city_weather_list.append(city_weather)

    pprint.pprint(city_weather_list)

    context = {
        'city_weather_list' : city_weather_list,
        'form': form
    }

    return render(request,'weather/home.html',context)