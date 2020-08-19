from django.contrib import admin
from .models import City

admin.site.site_title = 'Admin'
admin.site.site_header = 'MyWeatherApp Administration'
admin.site.index_title = 'MyWeather'

admin.site.register(City)