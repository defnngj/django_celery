from django.shortcuts import render
from django.http import JsonResponse
from .tasks import add


# Create your views here.

def index(request):
    add.delay(1, 2)
    return JsonResponse({'msg':'This is OK !'})
