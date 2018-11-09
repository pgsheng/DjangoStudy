"""
 接收用户的请求
 @Author  : pgsheng
 @Time    : 2018/11/9 14:50
"""
from django.http import HttpResponse
from django.shortcuts import render_to_response, render


# 表单,GET方法。视图显示(search_form)和请求处理(search)分成两个函数处理
def search_form(request):
    return render_to_response('search_form.html')


# 接收请求数据
def search(request):
    # request.encoding = 'utf-8'
    if 'q' in request.GET:
        message = '你搜索的内容为: ' + request.GET['q']
    else:
        message = '你提交了空表单'
    return HttpResponse(message)


# 接收POST请求数据
def search_post(request):
    ctx = {}
    if request.POST:
        ctx['rlt'] = request.POST['q']
    print("请求是否安全：%s" % request.is_secure())
    print("请求路径：%s" % request.get_full_path())
    return render(request, "post.html", ctx)
