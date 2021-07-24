"""
ASGI config for core project.
It exposes the ASGI callable as a module-level variable named ``application``.
For more information on this file, see
https://docs.djangoproject.com/en/3.2/howto/deployment/asgi/
"""

import os

from django.core.asgi import get_asgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')
from channels.routing import ProtocolTypeRouter, URLRouter
from django.urls import path
from home.consumers import *
application = get_asgi_application()


ws_patterns = [

    path('ws/django/' , NewConsumer )
    
]

application = ProtocolTypeRouter({
    'websocket' : URLRouter(ws_patterns)
})

#ws://127.0.0.1:8000/ws/django/