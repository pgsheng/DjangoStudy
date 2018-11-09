## 安装 Django 之后，会附带一个命令行工具django-admin,可以管理Django项目
## 使用django-admin来创建DjangoStudy项目：django-admin startproject DjangoStudy
    HelloWorld # 项目的容器
        __init__.py
        -- settings.py # 项目的设置/配置
        -- urls.py # 项目的 URL 声明; 一份由 Django 驱动的网站"目录"
        -- wsgi.py # WSGI兼容的Web服务器的入口，以便运行你的项目。
    -- manage.py # 一个实用的命令行工具，可让你以各种方式与该 Django 项目进行交互
## 运行Django项目,启动服务器： 
    python manage.py runserver
    (python manage.py runserver 127.0.0.1:8000) 指定一个 IP 地址
    通过http://127.0.0.1:8000/来访问正在运行的项目
## 创建app，Django项目，app表示更小一个功能单位，如博客管理系统中，对博客的增删查改等功能就应该聚合在一个app中。
        django-admin startapp hello
## settings配置文件中INSTALLED_APPS配置新建的APP
## DATABASES配置模型层（数据库）: python manage.py migrate 命令生成数据库表
    python manage.py makemigrations hello  # 让 Django 知道我们在我们的模型有一些变更
    python manage.py migrate hello   # 创建表结构



## 常见异常：
    1、django.core.exceptions.ImproperlyConfigured: Error loading MySQLdb module
        原因：python3改变连接库，改为pymysql库，Django中，连接数据库时使用的是MySQLdb库
        解决方法：在项目容器下 __init__.py 文件中添加以下代码即可。
            import pymysql
            pymysql.install_as_MySQLdb()
    2、You called this URL via POST, but the URL doesn't end in a slash and you have APPEND_SLASH set
        原因：post方式的urls.py路径配置和html的表单提交路径配置要一致（结尾都要‘/’或都不要）