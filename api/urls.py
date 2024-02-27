from django.urls import path
from . import views

app_name = 'api'


urlpatterns = [
    path('films/', views.FilmListView.as_view(), name='films'),
    path('add_film/', views.FilmCreateView.as_view(), name='add_films'),
]
