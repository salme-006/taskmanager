from django.shortcuts import render, get_object_or_404, redirect
from .models import Task
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


def task_edit(request, task_id):
    task = get_object_or_404(Task, id=task_id)  # پیدا کردن تسک بر اساس ID
    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)  # بارگذاری فرم با داده‌های تسک
        if form.is_valid():
            form.save()  # ذخیره تغییرات
            return redirect('task_list')  # برگشت به لیست تسک‌ها
    else:
        form = TaskForm(instance=task)  # بارگذاری فرم با داده‌های تسک

    return render(request, 'tasks/task_form.html', {'form': form})


def task_delete(request, task_id):
    task = get_object_or_404(Task, id=task_id)  # پیدا کردن تسک بر اساس ID
    task.delete()  # حذف تسک
    return redirect('task_list')  # برگشت به لیست تسک‌ها

# اضافه کردن view برای صفحه about
# def about(request):
#    return render(request, 'about.html')  # مسیر قالب باید وجود داشته باشد
