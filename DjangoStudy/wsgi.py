"""
个 WSGI 兼容的 Web 服务器的入口，以便运行你的项目
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'DjangoStudy.settings')

application = get_wsgi_application()
