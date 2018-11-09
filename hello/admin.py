from django.contrib import admin

from hello.models import Test, Contact, Tag

"""
为了让 admin 界面管理某个数据模型，我们需要先注册该数据模型到 admin,如
"""
# admin.site.register(Test)
admin.site.register([Test, Contact, Tag])