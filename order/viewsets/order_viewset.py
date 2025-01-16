from rest_framework.viewsets import ModelViewSet
<<<<<<< HEAD
=======
from rest_framework.authentication import SessionAuthentication, BasicAuthentication, TokenAuthentication
from rest_framework.permissions import IsAuthenticated
>>>>>>> f7c294766804d6077e22a61d40c5fcdba9c96cbd

from order.models import Order
from order.serializers import OrderSerializer


class OrderViewSet(ModelViewSet):
<<<<<<< HEAD

    serializer_class = OrderSerializer
    queryset = Order.objects.all().order_by("id")
=======
   authentication_classes = [SessionAuthentication, BasicAuthentication, TokenAuthentication]
   permission_classes = [IsAuthenticated]
   serializer_class = OrderSerializer
   queryset = Order.objects.all().order_by('id')
>>>>>>> f7c294766804d6077e22a61d40c5fcdba9c96cbd
