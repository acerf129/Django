from django.shortcuts import render
import json
import urllib.request
import ssl
# Create your views here.
def index(request):
    if request.method =='POST':
        city = request.POST['city'].upper()
        ssl._create_default_https_context = ssl._create_unverified_context
        try:
            res =urllib.request.urlopen('http://api.openweathermap.org/data/2.5/weather?q='+city+'&appid=beedf3a1ced85957c72b8c2a4e06b352').read()
            json_data = json.loads(res)
            print(json_data)
            data = {
                "country_code":str(json_data['sys']['country']),
                "coordinate":str(json_data['coord']['lon'])+' '+
                str(json_data['coord']['lat']),
                "temp":str(json_data['main']['temp'])+'k',
                "pressure":str(json_data['main']['pressure']),
                "humidity":str(json_data['main']['humidity']),
            }
        except:
            city='Search No Found'
            data={} 
    else:
        city=''
        data={} 
    return render(request,'index.html', {'city':city, "data":data}) 