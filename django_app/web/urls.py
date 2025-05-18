from django.urls import path
from .views import home_index, create_task, delete_task, abaout_us_view
from .views.collection import collection_index, create_collection, edit_collection, assign_task_collection, assigntask_collection
from . import views

urlpatterns = [
    path('', home_index, name='home'),
    path('task/create',create_task, name='create_task_post'),
    path('task/delete',delete_task, name='delete_task_post'),
    path('collection/', collection_index, name='collection'),
    path('collection/create', create_collection, name='collection_create'),
    path('collection/edit/<uuid:id>', edit_collection, name='collection_edit'),
    path('collection/edit', edit_collection, name='collection_editpost'),
    path('collection/assigntasks', assigntask_collection, name='collection_assign_post'),
    path('collection/assigntasks/<uuid:id>', assign_task_collection, name='collection_assign'),
    path('about-us/', abaout_us_view, name='about_us'),
]
