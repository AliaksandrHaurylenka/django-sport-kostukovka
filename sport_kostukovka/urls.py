from django.urls import path

from .views import *

urlpatterns = [
    path('', index, name='home'),
    path('news/', news, name='news'),
]