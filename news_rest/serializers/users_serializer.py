from news.models.user_model import Users
from rest_framework import serializers


class UsersSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Users
        fields = ["id", "name", "email", "role"]
