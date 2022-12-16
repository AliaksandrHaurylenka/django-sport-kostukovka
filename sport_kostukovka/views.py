from django.http import HttpResponse, Http404, HttpResponseNotFound
from django.shortcuts import render, redirect, get_object_or_404

from .forms import *
from .models import *


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


def addpage(request):
    posts = News.objects.all()
    if request.method == 'POST':
        form = AddPostForm(request.POST, request.FILES)
        if form.is_valid():
            # print(form.cleaned_data)
            form.save()
            return redirect('home')
    else:
        form = AddPostForm()
    # return render(request, 'women/addpage.html', {'form': form, 'menu': menu, 'title': 'Добавление статьи'})

    context = {
        'news': posts,
        'menu': menu,
        'form': form,
        'title': 'Добавление статьи'
    }
    return render(request, 'sport_kostukovka/addpage.html', context=context)


def sport_sections(request):
    return HttpResponse("Спортивные секции")


def contact(request):
    return HttpResponse("Обратная связь")


def login(request):
    return HttpResponse("Авторизация")


def show_news(request, post_slug):
    posts = News.objects.all()
    post = get_object_or_404(News, slug=post_slug)

    context = {
        'news': posts,
        'post': post,
        'menu': menu,
        'title': post.title,
        'cat_selected': post.cat_id,
    }

    return render(request, 'sport_kostukovka/post.html', context=context)


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
