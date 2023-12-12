from django.shortcuts import render
import json
import urllib.request
# Create your views here.


def index(request):
    if request.method == 'POST':
        city = request.POST['city']
        res = urllib.request.urlopen('https://api.weatherstack.com/current?access_key=556a2fdc7e96c5b37bda11bd113dc0ff&queary='+city)
        json_data = json.load(res)
        data = {
            'country_code': str(json_data['location']['country']),
            'coordinates': str(json_data['location']['lon']+ " " + str(json_data['location']['lat'])),
            'temp': int(json_data['current']['temperature']+'C'),
            'pressure': int(json_data['current']['pressure']+'C'),
            'humidity': int(json_data['current']['humidity']+'C')
            }
    else:
        data = {}
    return render(request, 'index.html')
