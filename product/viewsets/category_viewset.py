from rest_framework.viewsets import ModelViewSet

from product.models import Category
from product.serializers.category_serializer import CategorySerializer


class CategoryViewSet(ModelViewSet):
    serializer_class = CategorySerializer

    def get_queryset(self):
<<<<<<< HEAD
        return Category.objects.all().order_by("id")
=======
        return Category.objects.all().order_by('id')
>>>>>>> f7c294766804d6077e22a61d40c5fcdba9c96cbd
