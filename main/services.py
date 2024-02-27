from django.shortcuts import get_object_or_404
import requests
from .models import Director, Actor, Film
from django.conf import settings


def fill_data():
    ids = ['tt0111161', 'tt0068646', 'tt0468569', 'tt0071562', 'tt0050083',
           'tt0108052', 'tt0167260', 'tt0110912', 'tt0120737', 'tt0060196',
           'tt0109830', 'tt0167261', 'tt0137523', 'tt1375666', 'tt0080684',
           'tt0073486', 'tt0114369', 'tt0038650', 'tt0816692', 'tt0047478',
           'tt0102926', 'tt0120815', 'tt0317248', 'tt0118799', 'tt0120689',
           'tt0103064', 'tt0076759', 'tt0088763', 'tt0245429', 'tt0253474',]
    url = "http://www.omdbapi.com/"

    for id in ids:
        params = {'apikey': settings.OMDB_API_KEY, 'i': id}
        data = requests.get(url, params=params).json()
        
        _create_or_change_film(data['Title'], data['Year'], data['Director'], data['Actors'])


def add_film_to_db(data):
    _create_or_change_film(data.get('name'), data.get('year_of_release'), data.get('director'), data.get('actors'), data.get('id'))


def delete_film_from_db(film_id):
    film = get_object_or_404(Film, id=film_id)
    film.delete()


def _create_or_change_film(name, year, director, actors, id=None):
    if id:
        film = Film.objects.get(id=id)
        film.name = name
        film.year_of_release = year
        film.director = Director.objects.get_or_create(name=director)[0]
        for actor in film.actors.all():
            film.actors.remove(actor)
        film.save()
    else:
        film = Film.objects.create(
            name=name,
            year_of_release=year,
            director=Director.objects.get_or_create(name=director)[0],
        )
    
    actors_list = actors.split(', ')
    for actor_name in actors_list:
        actor = Actor.objects.get_or_create(name=actor_name)[0]
        film.actors.add(actor)
