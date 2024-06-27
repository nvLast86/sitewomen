from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.shortcuts import render, redirect
from datetime import datetime
from django.urls import reverse
from django.template.defaultfilters import slugify

menu=['О сайте','Добавить статью','Обратная связь','Войти']

data_db = [ {'id': 1, 'title': 'Анджелина Джоли', 'content': 'Биография Анджелины Джоли', 'is_published': True},
            {'id': 2, 'title': 'Марго Робби', 'content': 'Биография Марго Робби', 'is_published': False},
            {'id': 3, 'title': 'Джулия Робертс', 'content': 'Биография Джулии Робертс', 'is_published': True},
            ]


def index(request):
    data = {
        'title': 'главная страница',
        'menu': menu,
        'posts': data_db,
    }
    return render(request, 'women/index.html', context=data)


def about(request):
    data = {'author': 'Nikolay Lastenko'}
    return render(request, "women/about.html", context=data)


def categories(request, cat_id):
    return HttpResponse(f'<h1>Статьи по категориям</h1><p>id: {cat_id}</p>')


def categories_by_slug(request, cat_slug):
    return HttpResponse(f'<h1>Статьи по категориям</h1><p>slug: {cat_slug}</p>')


def archive(request, year):
    if year > datetime.now().year:
        uri = reverse('cats', args=('music', ))
        return redirect(uri)
        # raise Http404
    # return HttpResponse(f'<h1>Архив по годам</h1><p>{year}</p>')


def page_not_found(request, exception):
    return HttpResponseNotFound('<h1>Страница не найдена</h1>')
