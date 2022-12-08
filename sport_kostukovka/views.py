from django.http import HttpResponse
from django.shortcuts import render


menu = ["Новости", "Добавить статью", "Контакты", "Войти"]


def index(request):
    return render(request, 'kostukovka/index.html', {'menu': menu, 'title': 'Спорт-Костюковка'})


def news(request):
    return render(request, 'kostukovka/news.html', {'menu': menu, 'title': 'Новости'})
