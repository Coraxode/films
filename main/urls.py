from django.urls import path
from . import views

app_name = 'films'


urlpatterns = [
    path('', views.index, name='index'),
    path('fill_data/', views.fill_database, name='fill_data')
]
