from django.views.generic import ListView
from django.shortcuts import redirect
from .services import fill_data, delete_film_from_db
from .models import Film


class index(ListView):
    template_name = 'index.html'
    context_object_name = 'films'
    queryset = Film.objects.all()
    paginate_by = 25


def fill_database(request):
    fill_data()
    return redirect('films:index')


def delete_film(request, film_id):
    delete_film_from_db(film_id)
    return redirect('films:index')
