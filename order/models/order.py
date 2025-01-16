<<<<<<< HEAD
from django.db import models
from django.contrib.auth.models import User
=======
from django.contrib.auth.models import User
from django.db import models
>>>>>>> dc470303bf4b28221614af9800d5dea6727be939

from product.models import Product


class Order(models.Model):
    product = models.ManyToManyField(Product, blank=False)
<<<<<<< HEAD
    user = models.ForeignKey(User, on_delete=models.CASCADE)
=======
    user = models.ForeignKey(User, on_delete=models.CASCADE)
>>>>>>> dc470303bf4b28221614af9800d5dea6727be939
