"""
项目的 URL 声明; 一份由 Django 驱动的网站"目录"
"""
from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('admin/', admin.site.urls),
]
