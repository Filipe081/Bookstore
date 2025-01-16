<<<<<<< HEAD
#!/usr/bin/env python
# -*- coding: utf-8 -*-


=======
>>>>>>> f7c294766804d6077e22a61d40c5fcdba9c96cbd
from django.db import models

from product.models import Category

<<<<<<< HEAD

=======
>>>>>>> f7c294766804d6077e22a61d40c5fcdba9c96cbd
class Product(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(max_length=500, blank=True, null=True)
    price = models.PositiveIntegerField(null=True)
    active = models.BooleanField(default=True)
<<<<<<< HEAD
    category = models.ManyToManyField(Category, blank=True)


    def __str__(self):
        return self.title
=======
    category = models.ManyToManyField(Category, blank=True)
>>>>>>> f7c294766804d6077e22a61d40c5fcdba9c96cbd
