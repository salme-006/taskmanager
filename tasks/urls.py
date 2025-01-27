from django.urls import path
from . import views

urlpatterns = [
    path('', views.task_list, name='task_list'),  # مسیر لیست تسک‌ها
    path('create/', views.create_task, name='create_task'),  # مسیر ایجاد تسک
    path('tasks/', views.task_list, name='task_list'),
    path('tasks/edit/<int:task_id>/', views.task_edit, name='task_edit'),  # ویو ویرایش تسک
    path('tasks/delete/<int:task_id>/', views.task_delete, name='task_delete'),  # ویو حذف تسک
]
