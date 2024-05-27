from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.shortcuts import render, redirect
from datetime import datetime
from django.urls import reverse

menu=['О сайте','Добавить статью','Обратная связь','Войти']

class MyClass:

    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __str__(self):
        return f'объект с переменными {self.a} и {self.b}'


# Create your views here.
def index(request):
    data = {
        'title': 'Главная страница',
        'menu': menu,
        'float': 28.56,
        'lst': [1, 2, 'dff', True],
        'set': {1, 2, 3, 2},
        'dict': {'k': 'v', 'k2': 'v2'},
        'obj': MyClass(10,20)
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
