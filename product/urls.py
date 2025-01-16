<<<<<<< HEAD
#!/usr/bin/env python
# -*- coding: utf-8 -*-

=======
>>>>>>> f7c294766804d6077e22a61d40c5fcdba9c96cbd
from django.urls import include, path
from rest_framework import routers

from product import viewsets

router = routers.SimpleRouter()
router.register(r"product", viewsets.ProductViewSet, basename="product")
router.register(r"category", viewsets.CategoryViewSet, basename="category")

urlpatterns = [
    path("", include(router.urls)),
<<<<<<< HEAD
]
=======
]
>>>>>>> f7c294766804d6077e22a61d40c5fcdba9c96cbd
