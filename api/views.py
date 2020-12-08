from django.shortcuts import render
from django.http import JsonResponse
from api.tasks import add
from api.test_task import run_task


def index(request):
    add.delay(1, 2)
    return JsonResponse({'msg':'This is OK !'})


def task(request, rid):
    print("任务id", rid)
    run_task.delay()
    return JsonResponse({'msg': 'running'})
