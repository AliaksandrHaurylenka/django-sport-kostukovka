from django.http import HttpResponse
from django.shortcuts import render

from .models import *


menu = ["Спортивные секции", "Новости", "Контакты", "Войти"]


def index(request):
    return render(request, 'sport_kostukovka/index.html', {'menu': menu, 'title': 'Спорт-Костюковка'})


def news(request):
    news = News.objects.all()
    return render(request, 'sport_kostukovka/news.html', {'news': news, 'menu': menu, 'title': 'Новости'})
