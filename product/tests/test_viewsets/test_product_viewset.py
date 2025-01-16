import json

from django.urls import reverse
<<<<<<< HEAD
from rest_framework.authtoken.models import Token
=======

>>>>>>> f7c294766804d6077e22a61d40c5fcdba9c96cbd
from rest_framework.test import APIClient, APITestCase
from rest_framework.views import status

from order.factories import UserFactory
from product.factories import CategoryFactory, ProductFactory
from product.models import Product
<<<<<<< HEAD
=======
from rest_framework.authtoken.models import Token
>>>>>>> f7c294766804d6077e22a61d40c5fcdba9c96cbd


class TestProductViewSet(APITestCase):
    client = APIClient()

    def setUp(self):
        self.user = UserFactory()
<<<<<<< HEAD
        token = Token.objects.create(user=self.user)  # added
        token.save()  # added
=======
        token = Token.objects.create(user=self.user)
        token.save()
>>>>>>> f7c294766804d6077e22a61d40c5fcdba9c96cbd

        self.product = ProductFactory(
            title="pro controller",
            price=200.00,
        )

    def test_get_all_product(self):
<<<<<<< HEAD
        token = Token.objects.get(user__username=self.user.username)  # added
        self.client.credentials(
            HTTP_AUTHORIZATION="Token " + token.key)  # added
=======
        token = Token.objects.get(user__username=self.user.username)
        self.client.credentials(HTTP_AUTHORIZATION="Token " + token.key)
>>>>>>> f7c294766804d6077e22a61d40c5fcdba9c96cbd
        response = self.client.get(
            reverse("product-list", kwargs={"version": "v1"}))

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        product_data = json.loads(response.content)

<<<<<<< HEAD
        self.assertEqual(product_data["results"]
                         [0]["title"], self.product.title)
        self.assertEqual(product_data["results"]
                         [0]["price"], self.product.price)
        self.assertEqual(product_data["results"]
                         [0]["active"], self.product.active)
=======
        self.assertEqual(product_data['results'][0]["title"], self.product.title)
        self.assertEqual(product_data['results'][0]["price"], self.product.price)
        self.assertEqual(product_data['results'][0]["active"], self.product.active)
>>>>>>> f7c294766804d6077e22a61d40c5fcdba9c96cbd

    def test_create_product(self):
        token = Token.objects.get(user__username=self.user.username)
        self.client.credentials(HTTP_AUTHORIZATION="Token " + token.key)
<<<<<<< HEAD
        category = CategoryFactory()
        data = json.dumps(
            {"title": "notebook", "price": 800.00,
                "categories_id": [category.id]}
        )
=======

        category = CategoryFactory()
        data = json.dumps({
            "title": "notebook",
            "price": 800.00,
            "categories_id": [category.id]
        })
>>>>>>> f7c294766804d6077e22a61d40c5fcdba9c96cbd

        response = self.client.post(
            reverse("product-list", kwargs={"version": "v1"}),
            data=data,
            content_type="application/json",
        )

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        created_product = Product.objects.get(title="notebook")

        self.assertEqual(created_product.title, "notebook")
        self.assertEqual(created_product.price, 800.00)
