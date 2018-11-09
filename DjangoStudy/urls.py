"""
项目的 URL 声明; 一份由 Django 驱动的网站"目录"
Django >= 2.0 的版本，urls.py 的 django.conf.urls 已经被 django.urls 取代。
import url 变成了 import path,如果是路径，则须在路径后加个 /
"""
from django.urls import path

from hello import views, testdb

"""
url()可以接收四个参数，两个必选参数：regex、view 和两个可选参数：kwargs、name
regex: 正则表达式，与之匹配的 URL 会执行对应的第二个参数 view。
view: 用于执行与正则表达式匹配的 URL 请求。
kwargs: 视图使用的字典类型的参数。
name: 用来反向获取 URL。
"""
# urlpatterns = [ 旧版写法
#     url(r'^$', view.hello),   # http://127.0.0.1:8000/
#     url(r'^hello$', view.hello),  # http://127.0.0.1:8000/hello
# ]
urlpatterns = [
    path('', views.hello),
    path('hello/', views.hello),
    path('hello2/', views.hello2),
    path('testdb/', testdb.testdb_insert),
    path('testdb2/', testdb.testdb_select),
    path('testdb3/', testdb.testdb_update),
    path('testdb4/', testdb.testdb_delete),
]
