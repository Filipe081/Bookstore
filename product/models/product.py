<<<<<<< HEAD
=======
#!/usr/bin/env python
# -*- coding: utf-8 -*-


>>>>>>> dc470303bf4b28221614af9800d5dea6727be939
from django.db import models

from product.models import Category

<<<<<<< HEAD
=======

>>>>>>> dc470303bf4b28221614af9800d5dea6727be939
class Product(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(max_length=500, blank=True, null=True)
    price = models.PositiveIntegerField(null=True)
    active = models.BooleanField(default=True)
<<<<<<< HEAD
    category = models.ManyToManyField(Category, blank=True)
=======
    category = models.ManyToManyField(Category, blank=True)


    def __str__(self):
        return self.title
>>>>>>> dc470303bf4b28221614af9800d5dea6727be939
