from django.db import models


class Test(models.Model):
    """ 数据库模型
    类名代表了数据库的表名，类里面的字段代表数据表中的字段，数据类型则由CharField（相当于varchar）、
    DateField（相当于datetime）， max_length 参数限定长度
    """
    name = models.CharField(max_length=20)
