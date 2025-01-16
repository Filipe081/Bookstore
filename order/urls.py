<<<<<<< HEAD
#!/usr/bin/env python
# -*- coding: utf-8 -*-


=======
>>>>>>> f7c294766804d6077e22a61d40c5fcdba9c96cbd
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
>>>>>>> f7c294766804d6077e22a61d40c5fcdba9c96cbd
