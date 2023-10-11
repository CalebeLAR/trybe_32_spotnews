from django.shortcuts import render
from news.models.news_model import News


def home_page(request):
    context = {"news": News.objects.all()}
    return render(request, "home.html", context=context)
