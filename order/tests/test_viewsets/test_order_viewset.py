import json
<<<<<<< HEAD

from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient, APITestCase

=======
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient, APITestCase
>>>>>>> f7c294766804d6077e22a61d40c5fcdba9c96cbd
from order.factories import OrderFactory, UserFactory
from order.models import Order
from product.factories import CategoryFactory, ProductFactory
from product.models import Product
<<<<<<< HEAD


class TestOrderViewSet(APITestCase):

    client = APIClient()

    def setUp(self):
=======
from rest_framework.authtoken.models import Token


class TestOrderViewSet(APITestCase):
    client = APIClient()

    def setUp(self):
        self.user = UserFactory()  
        token = Token.objects.create(user=self.user)
        token.save()
>>>>>>> f7c294766804d6077e22a61d40c5fcdba9c96cbd
        self.category = CategoryFactory(title="technology")
        self.product = ProductFactory(
            title="mouse", price=100, category=[self.category]
        )
        self.order = OrderFactory(product=[self.product])

    def test_order(self):
<<<<<<< HEAD
        response = self.client.get(
            reverse("order-list", kwargs={"version": "v1"}))

        self.assertEqual(response.status_code, status.HTTP_200_OK)

        order_data = json.loads(response.content)
        self.assertEqual(
            order_data["results"][0]["product"][0]["title"], self.product.title
        )
        self.assertEqual(
            order_data["results"][0]["product"][0]["price"], self.product.price
        )
        self.assertEqual(
            order_data["results"][0]["product"][0]["active"], self.product.active
        )
        self.assertEqual(
            order_data["results"][0]["product"][0]["category"][0]["title"],
            self.category.title,
        )

    def test_create_order(self):
=======
        token = Token.objects.get(user__username=self.user.username)
        self.client.credentials(HTTP_AUTHORIZATION="Token " + token.key)
        response = self.client.get(
            reverse("order-list", kwargs={"version": "v1"})
        )

        self.assertEqual(response.status_code, status.HTTP_200_OK)

        try:
            order_data = json.loads(response.content)
        except json.JSONDecodeError:
            print("Erro ao decodificar JSON")
            print("Conteúdo da Resposta:", response.content)
            raise

        self.assertEqual(order_data['results'][0]["product"][0]["title"], self.product.title)
        self.assertEqual(order_data['results'][0]["product"][0]["price"], self.product.price)
        self.assertEqual(order_data['results'][0]["product"][0]["active"], self.product.active)
        self.assertEqual(
            order_data['results'][0]["product"][0]["category"][0]["title"],
            self.category.title
        )

    def test_create_order(self):
        token = Token.objects.get(user__username=self.user.username)
        self.client.credentials(HTTP_AUTHORIZATION="Token " + token.key)
>>>>>>> f7c294766804d6077e22a61d40c5fcdba9c96cbd
        user = UserFactory()
        product = ProductFactory()
        data = json.dumps({"products_id": [product.id], "user": user.id})

        response = self.client.post(
            reverse("order-list", kwargs={"version": "v1"}),
            data=data,
            content_type="application/json",
        )

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        created_order = Order.objects.get(user=user)
