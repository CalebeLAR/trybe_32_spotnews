from django.urls import path

from news.views import detais_page, home_page

urlpatterns = [
    path("", home_page, name="home-page"),
    path("news/<int:id>", detais_page, name="news-details-page"),
]
