from django.urls import path
from . import views

urlpatterns = [
    path('', views.task_list, name='task-list'),
    path('create/', views.create_task, name='create-task'),
]
