from django.db.models.query import QuerySet
from django.views.generic import ListView
from django.shortcuts import redirect
from .services import fill_data, delete_film_from_db, add_film_to_db
from .filters import FilmFilter
from .models import Film


class index(ListView):
    template_name = 'index.html'
    context_object_name = 'films'
    paginate_by = 25
    
    def get_queryset(self):
        self.film_filter = FilmFilter(self.request.GET, queryset=Film.objects.all())
        return self.film_filter.qs
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Films'
        context['form'] = self.film_filter.form
        return context


def fill_database(request):
    fill_data()
    return redirect('films:index')


def add_film(request):
    add_film_to_db(request.POST)
    return redirect('films:index')


def delete_film(request, film_id):
    delete_film_from_db(film_id)
    return redirect('films:index')
