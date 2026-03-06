import requests
from django.http import JsonResponse
from django.shortcuts import redirect


def dog_api(request):
    url = "https://dog.ceo/api/breeds/image/random"
    response = requests.get(url)
    data = response.json()
    return JsonResponse(data)   

def cat_api(request):
    url = "https://catfact.ninja/fact"
    response = requests.get(url)
    data = response.json()
    return JsonResponse(data)

def weather_api(request):
    url = "https://api.open-meteo.com/v1/forecast?latitude=14.6&longitude=121.0&current_weather=true"
    response = requests.get(url)
    data = response.json()
    return JsonResponse(data)

def joke_api(request):
    url = "https://official-joke-api.appspot.com/random_joke"
    response = requests.get(url)
    data = response.json()
    return JsonResponse(data)

def cat_img_api(request):
    url = "https://api.thecatapi.com/v1/images/search"
    response = requests.get(url)
    data = response.json()
    return redirect(data[0]["url"])
    
def duck_api(request):
    url = "https://some-random-api.com/animal/raccoon"
    response = requests.get(url)
    data = response.json()  
    return JsonResponse(data)

def fox_api(request):
    url = "https://randomfox.ca/floof/"
    response = requests.get(url)
    data = response.json()
    return JsonResponse(data)