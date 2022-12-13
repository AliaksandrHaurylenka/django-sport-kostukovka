from django.urls import path

from .views import *

urlpatterns = [
    path('', index, name='home'),
    path('sport_sections/', sport_sections, name='sport_sections'),
    path('news/', news, name='news'),
    path('contact/', contact, name='contact'),
    path('login/', login, name='login'),
    path('news/<int:news_id>/', show_news, name='news'),
    path('category/<int:cat_id>/', show_category, name='category'),
]