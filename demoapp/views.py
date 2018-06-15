from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.http import HttpResponse
import json

def Index(request):
    return render(request, 'index.html')


def Login(request):
    return render(request, 'login.html')

def getJson(request):
    resp = {'errorcode': 100, 'detail': 'Get success'}
    return HttpResponse(json.dumps(resp), content_type="application/json")
