from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST
from django.http import JsonResponse
from web.models import Task
import json

def home_index(request):
    items = Task.objects.all()
    return render(request,'home.html',{'items': items})
@require_POST
def create_task(request):
    data = json.loads(request.body)
    text_value = data.get('text')
    if not text_value:
        return JsonResponse({'ok':False,'message': 'Missing name field.'}, status=400)
    task = Task()
    task.text = text_value
    task.description = data.get('description')   
    task.save()
    return JsonResponse({'ok': True,'data':task.unique_id})
@require_POST
def delete_task(request):
    data = json.loads(request.body)
    id = data.get('id')
    task_to_delete = Task.objects.get(unique_id = id)
    if task_to_delete is None:
        return JsonResponse({'ok': False})
    task_to_delete.delete()
    return JsonResponse({'ok': True})
def task_form(request):
    items = Task.objects.all()
    return render(request,'taskform.html',{'items': items})
