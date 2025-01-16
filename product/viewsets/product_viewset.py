from rest_framework.viewsets import ModelViewSet

from product.models import Product
from product.serializers.product_serializer import ProductSerializer


class ProductViewSet(ModelViewSet):
    serializer_class = ProductSerializer

    def get_queryset(self):
<<<<<<< HEAD
        return Product.objects.all().order_by('id')
    
=======
        return Product.objects.all().order_by("id")
>>>>>>> dc470303bf4b28221614af9800d5dea6727be939
