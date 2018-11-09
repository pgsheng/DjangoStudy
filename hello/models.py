from django.db import models


class Test(models.Model):
    """ 数据库模型
    类名代表了数据库的表名，类里面的字段代表数据表中的字段，数据类型则由CharField（相当于varchar）、
    DateField（相当于datetime）， max_length 参数限定长度
    """
    name = models.CharField(max_length=20)

    def __str__(self):  # 作用是美化打印出来的结果，如你访问admin所看到的内容是否友好
        return self.name


class Contact(models.Model):
    name = models.CharField(max_length=200)
    age = models.IntegerField(default=0)
    email = models.EmailField()

    def __str__(self):
        return self.name


class Tag(models.Model):
    contact = models.ForeignKey(Contact, on_delete=models.CASCADE)  # 外键一对多
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name
