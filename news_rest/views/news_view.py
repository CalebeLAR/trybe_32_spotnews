from news.models.news_model import News
from news_rest.serializers.news_serializer import NewsSerializer
from rest_framework import viewsets


class NewsViewSet(viewsets.ModelViewSet):
    queryset = News.objects.all()
    serializer_class = NewsSerializer
