from django.urls import path

from news.views import details_page, home_page, categories_form_page, news_form_page

urlpatterns = [
    path("", home_page, name="home-page"),
    path("news/<int:id>", details_page, name="news-details-page"),
    path("categories/", categories_form_page, name="categories-form"),
    path("news/", news_form_page, name="news-form"),
]
