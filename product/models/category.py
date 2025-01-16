<<<<<<< HEAD
#!/usr/bin/env python
# -*- coding: utf-8 -*-

=======
>>>>>>> f7c294766804d6077e22a61d40c5fcdba9c96cbd
from django.db import models


class Category(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField(unique=True)
    description = models.CharField(max_length=200, blank=True, null=True)
    active = models.BooleanField(default=True)

<<<<<<< HEAD
    def __str__(self):
        return self.title
=======
    def __unicode__(self):
        return self.title
>>>>>>> f7c294766804d6077e22a61d40c5fcdba9c96cbd
