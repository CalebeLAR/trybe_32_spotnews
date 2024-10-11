from news.models.news_model import News
from rest_framework import serializers


class NewsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = News
        fields = [
            "id",
            "title",
            "content",
            "author",
            "created_at",
            "image",
            "categories",
        ]
