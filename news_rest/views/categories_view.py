from news.models.category_model import Categories
from news_rest.serializers.categories_serializer import CategoriesSerializer
from rest_framework import viewsets


class CategoriesViewSet(viewsets.ModelViewSet):
    queryset = Categories.objects.all()
    serializer_class = CategoriesSerializer
