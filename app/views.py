from django.http import HttpResponse
from django.shortcuts import render, reverse
from datetime import datetime
from os import listdir, getcwd


def home_view(request):
    template_name = 'home.html'
    pages = {
        'Главная страница': reverse('home'),
        'Показать текущее время': reverse('time'),
        'Показать содержимое рабочей директории': reverse('workdir'),
    }
    context = {
        'pages': pages
    }
    return render(request, template_name, context)


def time_view(request):
    current_time = datetime.now().time()
    msg = f'Текущее время: {current_time}'
    return HttpResponse(msg)


def workdir_view(request):
    try:
        files = [_ for _ in listdir(getcwd())]
        return HttpResponse('\n'.join(files))
    except BaseException:
        raise NotImplemented
