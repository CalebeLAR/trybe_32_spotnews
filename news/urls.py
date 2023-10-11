from django.urls import path

from news.views import home_page

urlpatterns = [
    path("", home_page, name="home-page"),
]
