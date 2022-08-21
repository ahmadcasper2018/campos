from django.urls import path
from .views import list_articles, article_detail, article_search, create

app_name = 'articles'

urlpatterns = [
    path('', list_articles, name='article_list'),
    path('article/<int:id>/', article_detail, name='article_detail'),
    path('search/', article_search, name='article_search'),
    path('create/', create, name='create'),


]
