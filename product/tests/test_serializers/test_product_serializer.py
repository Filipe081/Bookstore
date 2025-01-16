<<<<<<< HEAD
=======
#!/usr/bin/env python
# -*- coding: utf-8 -*-
>>>>>>> f7c294766804d6077e22a61d40c5fcdba9c96cbd
from django.test import TestCase

from product.factories import CategoryFactory, ProductFactory
from product.serializers import ProductSerializer


class TestProductSerializer(TestCase):
    def setUp(self) -> None:
<<<<<<< HEAD
        self.category = CategoryFactory(title="technology")
        self.product_1 = ProductFactory(
            title="mouse", price=100, category=[self.category]
        )
=======
        self.category = CategoryFactory(title='technology')
        self.product_1 = ProductFactory(title='mouse', price=100, category=[self.category])
>>>>>>> f7c294766804d6077e22a61d40c5fcdba9c96cbd
        self.product_serializer = ProductSerializer(self.product_1)

    def test_product_serializer(self):
        serializer_data = self.product_serializer.data
<<<<<<< HEAD
        self.assertEquals(serializer_data["price"], 100)
        self.assertEquals(serializer_data["title"], "mouse")
        self.assertEquals(
            serializer_data["category"][0]["title"], "technology")
=======
        self.assertEqual(serializer_data['price'], 100)
        self.assertEqual(serializer_data['title'], 'mouse')
        self.assertEqual(serializer_data['category'][0]['title'], 'technology')
>>>>>>> f7c294766804d6077e22a61d40c5fcdba9c96cbd
