from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

# Главная страница
def index(request):
    return HttpResponse('Главная')

def gruop_posts(request, slug):
    return HttpResponse(f'Посты, отфильтрованные по группе {slug}')

