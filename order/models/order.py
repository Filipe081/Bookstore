<<<<<<< HEAD
from django.contrib.auth.models import User
from django.db import models
=======
from django.db import models
from django.contrib.auth.models import User
>>>>>>> f7c294766804d6077e22a61d40c5fcdba9c96cbd

from product.models import Product


class Order(models.Model):
    product = models.ManyToManyField(Product, blank=False)
<<<<<<< HEAD
    user = models.ForeignKey(User, on_delete=models.CASCADE)
=======
    user = models.ForeignKey(User, on_delete=models.CASCADE)
>>>>>>> f7c294766804d6077e22a61d40c5fcdba9c96cbd
