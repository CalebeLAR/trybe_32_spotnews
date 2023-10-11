from django.shortcuts import redirect, render
from news.models.category_model import Categories
from news.models.news_model import News
from news.forms import CreateCategoryForm, CreateNewsModelForm


def home_page(request):
    context = {"news": News.objects.all()}
    return render(request, "home.html", context=context)


def details_page(request, id):
    context = {"new": News.objects.get(id=id)}
    return render(request, "news_details.html", context=context)


def categories_form_page(request):
    form = CreateCategoryForm()

    if request.method == "POST":
        form = CreateCategoryForm(request.POST)

        if form.is_valid():
            Categories.objects.create(**form.cleaned_data)

            return redirect("home-page")

    context = {"form": form}
    return render(request, "categories_form.html", context=context)


def news_form_page(request):
    form = CreateNewsModelForm()

    if request.method == "POST":
        form = CreateNewsModelForm(request.POST, request.FILES)

        if form.is_valid():
            news = form.save()
            news.categories.set(request.POST.getlist("categories"))
            news.save()

            return redirect("home-page")

    context = {"form": form}
    return render(request, "news_form.html", context=context)
