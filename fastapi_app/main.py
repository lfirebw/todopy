import os
import sys

# Find Django app from FastAPI
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'django_app')))
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings")

import django
django.setup()

from fastapi import FastAPI, HTTPException, Query, Path
from fastapi_app.schemas import TaskOut, CollectionOut 
from typing import List, Optional
from django.db.models import Q
from web.models import Task, Collection
from uuid import UUID


app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Hello FastAPI!"}
    
@app.get("/tasks", response_model=List[TaskOut])
def get_tasks(
    search: Optional[str] = Query(None, min_length=2),
    completed: Optional[bool] = Query(None),
    skip: int = Query(0, ge=0),
    limit: int = Query(10, le=100)
):
    filtros = Q()
    if search:
        filtros &= Q(text__icontains=search)
    if completed is not None:
        filtros &= Q(checked=completed)

    tasks = Task.objects.select_related("collection").filter(filtros)[skip:skip+limit]
    return list(tasks)

@app.get("/collections", response_model=List[CollectionOut])
def get_collections():
    return list(Collection.objects.all())

@app.get("/collections/{collection_id}", response_model=CollectionOut)
def get_collection_by_id(collection_id: UUID = Path(...)):
    try:
        return Collection.objects.get(unique_id=collection_id)
    except Collection.DoesNotExist:
        raise HTTPException(status_code=404, detail="Collection no encontrada")