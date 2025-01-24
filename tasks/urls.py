from django.urls import path
from . import views

urlpatterns = [
    path('', views.task_list, name='task_list'),  # مسیر لیست تسک‌ها
    path('create/', views.create_task, name='create_task'),  # مسیر ایجاد تسک
    path('about/', views.about, name='about'),  # مسیر صفحه درباره ما
    path('contact/', views.contact, name='contact'),  # مسیر صفحه تماس با ما
    path('post/', views.post, name='post'),  # مسیر صفحه تماس با ما
    path('index/', views.index, name='index'),  # مسیر صفحه تماس با ما
]
