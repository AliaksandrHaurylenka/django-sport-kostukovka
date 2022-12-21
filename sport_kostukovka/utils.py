from django.db.models import Count

from .models import *

menu = [{'title': "Спортивные секции", 'url_name': 'sport_sections'},
        {'title': "Новости", 'url_name': 'news'},
        {'title': "Контакты", 'url_name': 'contact'},
        {'title': "Войти", 'url_name': 'login'}
        ]


class DataMixin:
    def get_user_context(self, **kwargs):
        context = kwargs
        posts = News.objects.all()
        cats = Category.objects.annotate(Count('news'))

        # Если не авторизирован, то скрывает определенное меню
        # user_menu = menu.copy()
        # if not self.request.user.is_authenticated:
        #     user_menu.pop(1)

        # context['menu'] = user_menu
        context['menu'] = menu
        context['posts'] = posts
        context['cats'] = cats

        if 'cat_selected' not in context:
            context['cat_selected'] = 0
        return context
