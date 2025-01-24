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

# اضافه کردن view برای صفحه about
def about(request):
    return render(request, 'about.html')  # مسیر قالب باید وجود داشته باشد

# اضافه کردن view برای صفحه contact
def contact(request):
    return render(request, 'contact.html')  # مسیر قالب باید وجود داشته باشد

# اضافه کردن view برای صفحه post
def post(request):
    return render(request, 'post.html')  # مسیر قالب باید وجود داشته باشد

# اضافه کردن view برای صفحه index
def index(request):
    return render(request, 'index.html')  # مسیر قالب باید وجود داشته باشد
