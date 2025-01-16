"""
WSGI config for bookstore project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
<<<<<<< HEAD
https://docs.djangoproject.com/en/3.2/howto/deployment/wsgi/
=======
https://docs.djangoproject.com/en/5.0/howto/deployment/wsgi/
>>>>>>> f7c294766804d6077e22a61d40c5fcdba9c96cbd
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'bookstore.settings')

application = get_wsgi_application()
