from django.shortcuts import render
from .models import Article
from django.template.loader import render_to_string
from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth.decorators import login_required


def list_articles(request):
    articles = Article.objects.all()
    context = {
        "articles": articles,
    }
    articles_string = render_to_string('articles/articles_list.html', context=context)
    return HttpResponse(articles_string)


def article_detail(request, *args, **kwargs):
    pk = kwargs.pop('id')
    article = Article.objects.get(id=pk)
    context = {
        'article': article,
    }
    article_string = render_to_string('articles/article_detail.html', context)
    return HttpResponse(article_string)


def article_search(request):
    pk = request.GET.get('q')
    article = Article.objects.get(id=pk)
    context = {
        'article': article,
    }
    article_string = render_to_string('articles/article_search.html', context)
    return HttpResponse(article_string)


@login_required
def create(request):
    context = {}
    if request.method == "POST":
        data = request.POST
        title = data.get('title')
        content = data.get('content')
        article = Article.objects.create(title=title, content=content)
        context = {
            'article': article,
            'created': True,
        }

    return render(request, 'articles/create.html', context)
