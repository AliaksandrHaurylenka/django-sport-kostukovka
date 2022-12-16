from django.urls import path

from .views import *

urlpatterns = [
    path('', index, name='home'),
    path('sport_sections/', sport_sections, name='sport_sections'),
    path('news/', news, name='news'),
    path('addpage/', addpage, name='add_page'),
    path('contact/', contact, name='contact'),
    path('login/', login, name='login'),
    path('news/<slug:post_slug>/', show_news, name='post'),
    path('category/<int:cat_id>/', show_category, name='category'),
]