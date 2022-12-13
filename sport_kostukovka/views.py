from django.http import HttpResponse
from django.shortcuts import render

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
    news = News.objects.all()
    cats = Category.objects.all()

    context = {
        'news': news,
        'menu': menu,
        'cats': cats,
        'cat_selected': 0,
        'title': 'Спортивные события'
    }

    return render(request, 'sport_kostukovka/news.html', context=context)


def sport_sections(request):
    return HttpResponse("Добавление статьи")


def contact(request):
    return HttpResponse("Обратная связь")


def login(request):
    return HttpResponse("Авторизация")


def show_news(request, news_id):
    return HttpResponse(f"Отображение статьи с id = {news_id}")


def show_category(request, cat_id):
    return HttpResponse(f"Отображение категории с id = {cat_id}")
