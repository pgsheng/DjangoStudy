## 安装 Django 之后，会附带一个命令行工具django-admin,可以管理Django项目
## 使用django-admin来创建DjangoStudy项目：django-admin startproject DjangoStudy
    HelloWorld # 项目的容器
        __init__.py
        -- settings.py # 项目的设置/配置
        -- urls.py # 项目的 URL 声明; 一份由 Django 驱动的网站"目录"
        -- wsgi.py # WSGI兼容的Web服务器的入口，以便运行你的项目。
    -- manage.py # 一个实用的命令行工具，可让你以各种方式与该 Django 项目进行交互
## 运行Django项目,启动服务器： 
    python manage.py runserver 127.0.0.1:8000
    通过http://127.0.0.1:8000/来访问正在运行的项目
## 创建app，Django项目，app表示更小一个功能单位，如博客管理系统中，对博客的增删查改等功能就应该聚合在一个app中。
        django-admin startapp hello

## 常见异常：
    1、UnicodeDecodeError: 'gbk' codec can't decode byte 0xae in position 176: illegal multibyte sequence
       原因1：文件打开出现编码错误 ；原因2.  配置文件中 scrapy.cfg 含有中文字符