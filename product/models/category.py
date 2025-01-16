<<<<<<< HEAD
=======
#!/usr/bin/env python
# -*- coding: utf-8 -*-

>>>>>>> dc470303bf4b28221614af9800d5dea6727be939
from django.db import models


class Category(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField(unique=True)
    description = models.CharField(max_length=200, blank=True, null=True)
    active = models.BooleanField(default=True)

<<<<<<< HEAD
    def __unicode__(self):
        return self.title
=======
    def __str__(self):
        return self.title
>>>>>>> dc470303bf4b28221614af9800d5dea6727be939
