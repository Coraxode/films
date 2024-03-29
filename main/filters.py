import django_filters
from .models import Film


class FilmFilter(django_filters.FilterSet):
    class Meta:
        model = Film
        fields = {
            'year_of_release': ['lt', 'gt'],
            'director': ['exact'],
            'actors': ['exact']
        }
