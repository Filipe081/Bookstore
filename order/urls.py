<<<<<<< HEAD
=======
#!/usr/bin/env python
# -*- coding: utf-8 -*-


>>>>>>> dc470303bf4b28221614af9800d5dea6727be939
from django.urls import include, path
from rest_framework import routers

from order import viewsets

router = routers.SimpleRouter()
router.register(r"order", viewsets.OrderViewSet, basename="order")


urlpatterns = [
    path("", include(router.urls)),
<<<<<<< HEAD
]
=======
]
>>>>>>> dc470303bf4b28221614af9800d5dea6727be939
