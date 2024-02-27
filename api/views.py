from rest_framework.response import Response
from rest_framework import generics, status
from main.models import Film
from .serializers import FilmSerializer, FilmValidateSerializers
from main.services import add_film_to_db


class FilmListView(generics.ListAPIView):
    queryset = Film.objects.all()
    serializer_class = FilmSerializer


class FilmCreateView(generics.CreateAPIView):
    queryset = Film.objects.all()
    serializer_class = FilmSerializer

    def post(self, request, *args, **kwargs):
        serializer = FilmValidateSerializers(data=request.data)
        serializer.is_valid(raise_exception=True)
        add_film_to_db(serializer.data)
        
        return Response(serializer.data, status=status.HTTP_201_CREATED)
