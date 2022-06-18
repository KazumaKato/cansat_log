from time import strftime
from django.shortcuts import render
from typing import cast
import requests
import random
from django.http import HttpResponse
import datetime


def getdata(request):
    time = datetime.datetime.now()
    strtime = time.strftime('%Y/%m/%d %H:%M:%S')
    return HttpResponse('Hello! It is '+ strtime +' in UK now! Raspberry Pi is working now...')
# Create your views here.
