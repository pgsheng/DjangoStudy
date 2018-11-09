"""
 @Author  : pgsheng
 @Time    : 2018/11/9 10:10
"""
from django.http import HttpResponse

from DjangoStudy.public.Log import Log
from hello.models import Test

log = Log().get_logger()


# 数据库操作
def testdb_insert(request):
    list = ['runoob', 'QQ', 'facebook', 'weixin']
    for name in list:
        test1 = Test(name=name)
        test1.save()  # 相当于SQL中的INSERT，网页请求一次就插入一次数据
    return HttpResponse("<p>数据添加成功！</p>")


def testdb_select(request):
    response = ''
    # 通过objects这个模型管理器的all()获得所有数据行，相当于SQL中的SELECT * FROM,返回的是QuerySet对象
    list1 = Test.objects.all()
    # list1 = Test.objects.all()[0:4]
    # 输出所有数据
    response1 = '1：'
    for var in list1:
        response1 += var.name + " "
    response += "<p>" + response1 + "</p>"

    try:
        # filter相当于SQL中的WHERE，可设置条件过滤结果,返回QuerySet对象()，不存在返回[]
        list2 = Test.objects.filter(id=8)
        # 输出所有数据
        response2 = '2：'
        for var in list2:
            response2 += var.name + " "
        response += "<p>" + response2 + "</p>"

        # get返回的是单个Model对象，记录不存在，报错
        response3 = Test.objects.get(id=9)
        response += "<p>3：" + response3.name + "</p>"
    except Exception as e:
        print('id不存在：%s' % e)

    # 限制返回的数据 相当于 SQL 中的 OFFSET 0 LIMIT 2;
    list4 = Test.objects.order_by('name')[0:2]
    response4 = '4：'
    for var in list4:
        response4 += var.name + " "
    response += "<p>" + response4 + "</p>"

    # 数据排序
    list5 = Test.objects.order_by("name")
    response5 = '5：'
    for var in list5:
        response5 += var.name + " "
    response += "<p>" + response5 + "</p>"

    # 上面的方法可以连锁使用
    list6 = Test.objects.filter(name="runoob").order_by("id")
    response6 = '6：'
    for var in list6:
        response6 += var.name + " "
    response += "<p>" + response6 + "</p>"

    return HttpResponse(response)


def testdb_update(request):
    # 修改其中一个id=1的name字段，再save，相当于SQL中的UPDATE
    test1 = Test.objects.get(id=11)
    test1.name = 'Google'
    test1.save()
    # 另外一种方式,get返回是Model对象，没有update()方法
    Test.objects.filter(id=11).update(name='weixin')
    # 修改所有的列
    # Test.objects.all().update(name='Google')

    return HttpResponse("<p>修改成功</p>")


def testdb_delete(request):
    # 删除id=1的数据
    Test.objects.get(id=10).delete()
    # 另外一种方式
    # Test.objects.filter(id=1).delete()
    # 删除所有数据
    # Test.objects.all().delete()
    return HttpResponse("<p>删除成功</p>")
