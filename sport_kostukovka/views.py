from django.http import HttpResponse, Http404, HttpResponseNotFound
from django.shortcuts import render, redirect, get_object_or_404

from .models import *


# menu = ["Спортивные секции", "Новости", "Контакты", "Войти"]
menu = [{'title': "Спортивные секции", 'url_name': 'sport_sections'},
        {'title': "Новости", 'url_name': 'news'},
        {'title': "Контакты", 'url_name': 'contact'},
        {'title': "Войти", 'url_name': 'login'}
]


def index(request):
    news = News.objects.all()
    return render(request, 'sport_kostukovka/index.html', {'news': news, 'menu': menu, 'title': 'Спорт-Костюковка'})


def news(request):
    posts = News.objects.all()
    cats = Category.objects.all()

    context = {
        'news': posts,
        'menu': menu,
        'cats': cats,
        'cat_selected': 0,
        'title': 'Спортивные события'
    }

    return render(request, 'sport_kostukovka/news.html', context=context)


def sport_sections(request):
    return HttpResponse("Спортивные секции")


def contact(request):
    return HttpResponse("Обратная связь")


def login(request):
    return HttpResponse("Авторизация")


def show_news(request, post_id):
    return HttpResponse(f"Отображение статьи с id = {post_id}")


def show_category(request, cat_id):
    posts = News.objects.filter(cat_id=cat_id)
    cats = Category.objects.all()

    if len(posts) == 0:
        raise Http404()

    context = {
        'news': posts,
        'menu': menu,
        'cats': cats,
        'title': 'Спортивные события',
        'cat_selected': cat_id,
    }

    return render(request, 'sport_kostukovka/news.html', context=context)
