<<<<<<< HEAD
from django.test import TestCase

from product.factories import CategoryFactory, ProductFactory
=======
#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.test import TestCase

from product.factories import ProductFactory, CategoryFactory
>>>>>>> f7c294766804d6077e22a61d40c5fcdba9c96cbd
from product.serializers import CategorySerializer


class TestCategorySerializer(TestCase):
    def setUp(self) -> None:
<<<<<<< HEAD
        self.category = CategoryFactory(title="food")
=======
        self.category = CategoryFactory(title='food')
>>>>>>> f7c294766804d6077e22a61d40c5fcdba9c96cbd
        self.category_serializer = CategorySerializer(self.category)

    def test_order_serializer(self):
        serializer_data = self.category_serializer.data

<<<<<<< HEAD
        self.assertEquals(serializer_data["title"], "food")
=======
        self.assertEqual(serializer_data['title'], 'food')
>>>>>>> f7c294766804d6077e22a61d40c5fcdba9c96cbd
