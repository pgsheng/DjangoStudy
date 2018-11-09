"""
项目的 URL 声明; 一份由 Django 驱动的网站"目录"
Django >= 2.0 的版本，urls.py 的 django.conf.urls 已经被 django.urls 取代。
import url 变成了 import path,如果是路径，则须在路径后加个 /
"""
from django.contrib import admin
from django.urls import path

from hello import views, testdb, search

urlpatterns = [
    path('admin/', admin.site.urls),  # 管理工具页面
    path('', views.hello),  # 调用方法不带括号
    path('hello/', views.hello),
    path('hello2/', views.hello2),
    path('testdb/', testdb.testdb_insert),
    path('testdb2/', testdb.testdb_select),
    path('testdb3/', testdb.testdb_update),
    path('testdb4/', testdb.testdb_delete),
    path('search-form/', search.search_form),
    path('search/', search.search),
    path('search-post/', search.search_post),
]
