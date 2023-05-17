from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import APOD
from rest_framework import status
import requests
import json
# Create your views here.
def getAPOD(request):
    api_key = 'obqnTJeViwbIIs5BUhq6bnNApif8M5s4dqw4tPef'
    get_nasa_apod = requests.get('https://api.nasa.gov/planetary/apod?api_key=' + api_key)
    context = {
            "apod": get_nasa_apod.json()
            }
    return render(request, 'api/index.html', context)