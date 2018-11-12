from django.contrib import admin

from hello.models import Test, Contact, Tag

"""
注册数据模型，自定义admin管理页面，栏目、列表、关联显示
"""


# admin.site.register(Test)
# admin.site.register([Test, Contact, Tag])

class TagInline(admin.TabularInline):  # 配置内联显示，两个表有外键关联，配置后可在同编辑页面上显示
    model = Tag


# 自定义管理页面，来取代默认的页面。比如上面的 "add" 页面。我们想只显示 name 和 email 部分
class ContactAdmin(admin.ModelAdmin):
    # fields = ('name', 'email')  # 定义了要显示的字段

    list_display = ('name', 'age', 'email')  # 配置数据查看页显示更多的数据栏目，默认只显示name
    search_fields = ('name',)  # 列表页增加搜索栏，搜索功能在管理大量记录时非常有
    inlines = [TagInline]  # 内联显示

    """我们还可以将输入栏分块，每个栏也可以定义自己的格式"""
    fieldsets = (
        ['Main', {
            'fields': ('name', 'email'),
        }],
        ['Advance', {
            'classes': ('collapse',),  # CSS样式，可折叠或展开
            'fields': ('age',),
        }]
    )


admin.site.register(Contact, ContactAdmin)
admin.site.register([Test, Tag])
