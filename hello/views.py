from django.shortcuts import render
"""

"""

def hello(request):
    # return HttpResponse("Hello world !!! ") # 直接输出到网页
    context = dict()
    context['hello'] = 'Hello World!'
    return render(request, 'hello.html', context)  # 通过模板输出数据，实现数据与视图分离


def hello2(request):
    return render(request, 'hello2.html')  # 通过模板输出数据，实现数据与视图分离
