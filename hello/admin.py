from django.contrib import admin

from hello.models import Test, Contact, Tag

"""
为了让 admin 界面管理某个数据模型，我们需要先注册该数据模型到 admin,如
"""


# admin.site.register(Test)
# admin.site.register([Test, Contact, Tag])

# 自定义管理页面，来取代默认的页面。比如上面的 "add" 页面。我们想只显示 name 和 email 部分
class ContactAdmin(admin.ModelAdmin):
    fields = ('name', 'email')


admin.site.register(Contact, ContactAdmin)
admin.site.register([Test, Tag])
