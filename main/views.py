from django.shortcuts import redirect, render
from .services import fill_data


def index(request):
    context = {
        'title': 'Films'
    }
    
    return render(request, 'index.html', context)


def fill_database(request):
    fill_data()
    return redirect('films:index')
