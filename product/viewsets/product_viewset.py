from rest_framework.viewsets import ModelViewSet

from product.models import Product
from product.serializers.product_serializer import ProductSerializer


class ProductViewSet(ModelViewSet):
    serializer_class = ProductSerializer

    def get_queryset(self):
<<<<<<< HEAD
        return Product.objects.all().order_by("id")
=======
        return Product.objects.all().order_by('id')
    
>>>>>>> f7c294766804d6077e22a61d40c5fcdba9c96cbd
