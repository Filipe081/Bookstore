<<<<<<< HEAD
#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.test import TestCase

from product.factories import ProductFactory, CategoryFactory
=======
from django.test import TestCase

from product.factories import CategoryFactory, ProductFactory
>>>>>>> dc470303bf4b28221614af9800d5dea6727be939
from product.serializers import CategorySerializer


class TestCategorySerializer(TestCase):
    def setUp(self) -> None:
<<<<<<< HEAD
        self.category = CategoryFactory(title='food')
=======
        self.category = CategoryFactory(title="food")
>>>>>>> dc470303bf4b28221614af9800d5dea6727be939
        self.category_serializer = CategorySerializer(self.category)

    def test_order_serializer(self):
        serializer_data = self.category_serializer.data

<<<<<<< HEAD
        self.assertEqual(serializer_data['title'], 'food')
=======
        self.assertEquals(serializer_data["title"], "food")
>>>>>>> dc470303bf4b28221614af9800d5dea6727be939
