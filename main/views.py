from django.shortcuts import redirect, render
from .services import fill_data, delete_film_from_db
from .models import Film


def index(request):
    context = {
        'title': 'Films',
        'films': Film.objects.all(),
    }
    
    return render(request, 'index.html', context)


def fill_database(request):
    fill_data()
    return redirect('films:index')


def delete_film(request, film_id):
    delete_film_from_db(film_id)
    return redirect('films:index')
