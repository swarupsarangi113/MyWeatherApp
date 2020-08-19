from .models import City
from django.forms import ModelForm,TextInput

class AddCityForm(ModelForm) :
    class Meta :
        model = City
        fields = ['city_name']
        widgets = {'city_name': TextInput(attrs={'class':'input','placeholder':'Enter City Name...','size':40})}