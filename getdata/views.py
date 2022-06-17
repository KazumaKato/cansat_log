from django.shortcuts import render
from typing import cast
import requests
import random
from django.http import HttpResponse


def getdata(request):
    data = random.random()
    return HttpResponse(data)

# Create your views here.
