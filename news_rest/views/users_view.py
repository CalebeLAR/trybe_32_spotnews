from news.models.user_model import Users
from news_rest.serializers.users_serializer import UsersSerializer
from rest_framework import viewsets


class UsersViewSet(viewsets.ModelViewSet):
    queryset = Users.objects.all()
    serializer_class = UsersSerializer
