from django.urls import path
from . import views

app_name = 'films'


urlpatterns = [
    path('', views.index.as_view(), name='index'),
    path('data/<str:action>', views.change_data, name='change_data'),
    path('add/', views.add_film, name='add'),
    path('<int:film_id>/delete/', views.delete_film, name='delete'),
]
