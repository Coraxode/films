from django.urls import path
from . import views

app_name = 'films'


urlpatterns = [
    path('', views.index.as_view(), name='index'),
    path('fill_data/', views.fill_database, name='fill_data'),
    path('<int:film_id>/delete/', views.delete_film, name='delete'),
]
