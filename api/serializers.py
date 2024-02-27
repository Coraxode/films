from rest_framework import serializers
from main.models import Film


class FilmSerializer(serializers.ModelSerializer):
    class Meta:
        model = Film
        fields = '__all__'


class FilmValidateSerializers(serializers.ModelSerializer):
    director = serializers.CharField(max_length=60)
    actors = serializers.CharField()
    
    class Meta:
        model = Film
        fields = '__all__'
