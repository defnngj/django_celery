from django.shortcuts import render
from django.http import JsonResponse
from api.tasks import add
from api.test_task import run_task


def index(request):
    add.delay(1, 2)
    return JsonResponse({'msg':'This is OK !'})


def interface_data():
    """
    定义接口数据
    """
    data_list = [
        ("http://httpbin.org/get", "get", {"params": {'key': 'value'}}, "resp"),
        ("http://httpbin.org/post", "post", {"data": {'key': 'value'}}, "resp"),
    ]
    return data_list


def task(request, tid):
    print("任务id", tid)
    data = interface_data()
    run_task.delay(tid, data)
    return JsonResponse({'msg': 'running'})
