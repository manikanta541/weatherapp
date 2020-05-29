from django.shortcuts import render
from . import views
from django.http import HttpResponse
import requests
# Create your views here.
def hello(request):
    
    return render(request,'temperature.html')
# def out(request):
#     # city = 'Las Vegas'
#     url = 'http://samples.openweathermap.org/data/2.5/weather?q=London,uk&appid=439d4b804bc8187953eb36d2a8c26a02'
#     r=requests.get(url).json()
    
#     cw = {
#         'city' : r['name'],
#         'temperature' : r['main']['temp']
#     }
#     print(cw['city'])
#     num1=request.POST['n1']
#     num2=request.POST['n2']
#     if(request.POST['dd'] == 'add'):
#         n3=int(num1)+int(num2)
#     elif(request.POST['dd'] == 'sub'):
#         n3=int(num1)-int(num2)
#     elif(request.POST['dd'] == 'mul'):
#         n3=int(num1)*int(num2)
#     else:
#         n3=int(num1)/int(num2)
#     return render(request,'result.html',{'n3':n3})
def temp(request):
    url = 'http://api.openweathermap.org/data/2.5/weather?q={}&units=imperial&appid=b6a6d567ade38a12d5ac871fe976b307'
    city = request.POST['cname']
    s=requests.get(url.format(city))
    print(s.text)
    r=requests.get(url.format(city)).json()  
    if r['cod']==404:
        print(False)
    else:
        cw = {
            'city' : city,
            'temperature' : r['main']['temp'],
            'desc' : r['weather'][0]['description'],
            'icon' : r['weather'][0]['icon'],
            'press' : r['main']['pressure'],
            'hum' : r['main']['humidity']
        }

    cw1 = {'cityw':cw}
    return render(request,'result.html',cw1)
    #{'city':cw['city'],'temp' : cw['temperature'],'desc' : cw['desc']}
