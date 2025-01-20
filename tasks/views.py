from django.shortcuts import render, redirect
from .forms import TaskForm

# Create your views here.

from .models import Task

def task_list(request):
    tasks = Task.objects.all()  # تمام تسک‌ها از پایگاه داده
    return render(request, 'tasks/task_list.html', {'tasks': tasks})


def create_task(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('task-list')  # بعد از ذخیره برمی‌گرده به صفحه لیست وظایف
    else:
        form = TaskForm()

    return render(request, 'tasks/create_task.html', {'form': form})
