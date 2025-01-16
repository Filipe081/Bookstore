<<<<<<< HEAD
=======
#!/usr/bin/env python
# -*- coding: utf-8 -*-

>>>>>>> dc470303bf4b28221614af9800d5dea6727be939
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
>>>>>>> dc470303bf4b28221614af9800d5dea6727be939
