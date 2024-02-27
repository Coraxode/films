from rest_framework import serializers
from main.models import Film, Actor


class ActorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Actor
        fields = ['name']


class FilmSerializer(serializers.ModelSerializer):
    director = serializers.CharField(source='director.name')
    actors = serializers.SerializerMethodField()

    class Meta:
        model = Film
        fields = '__all__'

    def get_actors(self, obj):
        return ', '.join([actor.name for actor in obj.actors.all()])


class FilmValidateSerializer(serializers.ModelSerializer):
    director = serializers.CharField(max_length=60)
    actors = serializers.CharField()
    
    class Meta:
        model = Film
        fields = '__all__'
