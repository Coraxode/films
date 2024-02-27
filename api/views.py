from rest_framework.response import Response
from rest_framework import generics, status
from rest_framework.pagination import PageNumberPagination
from django_filters.rest_framework import DjangoFilterBackend
from main.models import Film
from main.filters import FilmFilter
from .serializers import FilmSerializer, FilmValidateSerializer
from main.services import add_film_to_db


class FilmListView(generics.ListAPIView):
    serializer_class = FilmSerializer
    pagination_class = PageNumberPagination
    pagination_class.page_size = 25
    filter_backends = (DjangoFilterBackend, )
    
    def get_queryset(self):
        self.film_filter = FilmFilter(self.request.GET, queryset=Film.objects.all())
        return self.film_filter.qs


class FilmCreateView(generics.CreateAPIView):
    queryset = Film.objects.all()
    serializer_class = FilmSerializer

    def post(self, request, *args, **kwargs):
        serializer = FilmValidateSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        add_film_to_db(serializer.data)
        
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class FilmRetrieveView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Film.objects.all()
    serializer_class = FilmSerializer
    
    def put(self, request, *args, **kwargs):
        return self.update_film(request, *args, **kwargs)

    def patch(self, request, *args, **kwargs):
        return self.update_film(request, *args, **kwargs)

    def update_film(self, request, *args, **kwargs):
        serializer = FilmValidateSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        data = dict(serializer.data)
        data['id'] = kwargs['pk']
        add_film_to_db(data)

        return Response(serializer.data, status=status.HTTP_201_CREATED)
