from django.shortcuts import render
from news.models.news_model import News


def home_page(request):
    context = {"news": News.objects.all()}
    return render(request, "home.html", context=context)


def detais_page(request, id):
    context = {"new": News.objects.get(id=id)}
    return render(request, "news_details.html", context=context)
