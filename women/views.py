from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.shortcuts import render, redirect
from datetime import datetime
from django.urls import reverse


# Create your views here.
def index(request):
    return HttpResponse('Страница приложения women')


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
