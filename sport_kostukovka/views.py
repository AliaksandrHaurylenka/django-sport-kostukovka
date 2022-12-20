from django.http import HttpResponse, Http404, HttpResponseNotFound
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView

from .forms import *
from .models import *


menu = [{'title': "Спортивные секции", 'url_name': 'sport_sections'},
        {'title': "Новости", 'url_name': 'news'},
        {'title': "Контакты", 'url_name': 'contact'},
        {'title': "Войти", 'url_name': 'login'}
]


def index(request):
    posts = News.objects.all()
    return render(request, 'sport_kostukovka/index.html', {'posts': posts, 'menu': menu, 'title': 'Спорт-Костюковка'})


class SportKostukovkaNews(ListView):
    model = News
    template_name = 'sport_kostukovka/news.html'
    context_object_name = 'posts'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['menu'] = menu
        context['title'] = 'Спортивные события'
        context['cat_selected'] = 0
        return context

    def get_queryset(self):
        return News.objects.filter(is_published=True)
# def news(request):
#     posts = News.objects.all()
#     cats = Category.objects.all()
#
#     context = {
#         'news': posts,
#         'menu': menu,
#         'cats': cats,
#         'cat_selected': 0,
#         'title': 'Спортивные события'
#     }
#
#     return render(request, 'sport_kostukovka/news.html', context=context)


class AddPage(CreateView):
    form_class = AddPostForm
    template_name = 'sport_kostukovka/addpage.html'
    context_object_name = 'posts'
    success_url = reverse_lazy('home')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Добавление статьи'
        context['menu'] = menu
        return context
# def addpage(request):
#     posts = News.objects.all()
#     if request.method == 'POST':
#         form = AddPostForm(request.POST, request.FILES)
#         if form.is_valid():
#             # print(form.cleaned_data)
#             form.save()
#             return redirect('home')
#     else:
#         form = AddPostForm()
#
#     context = {
#         'posts': posts,
#         'menu': menu,
#         'form': form,
#         'title': 'Добавление статьи'
#     }
#     return render(request, 'sport_kostukovka/addpage.html', context=context)


def sport_sections(request):
    return HttpResponse("Спортивные секции")


def contact(request):
    return HttpResponse("Обратная связь")


def login(request):
    return HttpResponse("Авторизация")


class ShowPost(DetailView):
    model = News
    template_name = 'sport_kostukovka/post.html'
    slug_url_kwarg = 'post_slug'
    context_object_name = 'post'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = context['post']
        context['menu'] = menu
        # context['posts'] = posts
        return context

# def show_news(request, post_slug):
#     posts = News.objects.all()
#     post = get_object_or_404(News, slug=post_slug)
#
#     context = {
#         'posts': posts,
#         'post': post,
#         'menu': menu,
#         'title': post.title,
#         'cat_selected': post.cat_id,
#     }
#
#     return render(request, 'sport_kostukovka/post.html', context=context)


class SportKostukovkaCategory(ListView):
    model = News
    template_name = 'sport_kostukovka/news.html'
    context_object_name = 'posts'
    allow_empty = False

    def get_queryset(self):
        return News.objects.filter(cat__slug=self.kwargs['cat_slug'], is_published=True)

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Категория - ' + str(context['posts'][0].cat)
        context['menu'] = menu
        context['cat_selected'] = context['posts'][0].cat_id
        return context


# def show_category(request, cat_id):
#     posts = News.objects.filter(cat_id=cat_id)
#     # cats = Category.objects.all()
#
#     if len(posts) == 0:
#         raise Http404()
#
#     context = {
#         'posts': posts,
#         'menu': menu,
#         # 'cats': cats,
#         'title': 'Спортивные события',
#         'cat_selected': cat_id,
#     }
#
#     return render(request, 'sport_kostukovka/news.html', context=context)
