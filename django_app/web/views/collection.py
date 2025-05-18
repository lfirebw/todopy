from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST
from django.http import JsonResponse
from web.models import Collection, Task
import json

def collection_index(request):
    items = Collection.objects.all()
    return render(request,'collection.html', {'collections': items})
def create_collection(request):
    if request.method == 'POST':
        name = request.POST['name']
        color = request.POST['color']
        Collection.objects.create(name = name, color = color)
        return redirect('collection')
    return render(request, 'create-collection.html')
@require_POST
def create(request):
    return redirect('collection_index')
def edit_collection(request,id=None):
    if request.method == 'POST':
        id = request.POST['id']
        item = Collection.objects.get(unique_id = id)
        item.name = request.POST['name']
        item.color = request.POST['color']
        item.save()
        return redirect('collection')
    if id == None:
        return redirect('collection')
    item = get_object_or_404(Collection, unique_id = id)
    return render(request,'edit-collection.html', {'collection': item})
def delete_collection(request):
    return redirect('collection_index')
def assign_task_collection(request, id):
    item_collection = Collection.objects.get(unique_id = id)
    # items_task = Task.objects.exclude(text__isnull = True)
    items_task = Task.objects.all()
    return render(request,'collection-assign.html', { 'collection': item_collection, 'tasks': items_task })
@require_POST
def assigntask_collection(request):
    data = json.loads(request.body)
    id_collection = data.get('id')
    if not id_collection:
        return JsonResponse({'ok': False})
    collection = Collection.objects.get(unique_id = id_collection)
    if not collection:
        return JsonResponse({'ok': False})
    #to do...

    return JsonResponse({'ok': True})