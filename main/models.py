from django.db import models


class Director(models.Model):
    first_name = models.CharField(max_length=60, help_text="Director first name")
    last_name = models.CharField(max_length=60, help_text="Director last name")
    
    class Meta:
        db_table = 'director'
        verbose_name = 'director'
        verbose_name_plural = 'directors'

    def __str__(self):
        return f'{self.first_name} {self.last_name}'


class Actor(models.Model):
    first_name = models.CharField(max_length=60, help_text="Actor first name")
    last_name = models.CharField(max_length=60, help_text="Actor last name")
    
    class Meta:
        db_table = 'actor'
        verbose_name = 'actor'
        verbose_name_plural = 'actors'

    def __str__(self):
        return f'{self.first_name} {self.last_name}'


class Film(models.Model):
    name = models.CharField(max_length=60, help_text="Film name")
    year_of_release = models.IntegerField(help_text="Film release year")
    director = models.ForeignKey(Director, on_delete=models.DO_NOTHING, help_text="Film director")
    actors = models.ManyToManyField(Actor, help_text="List of actors")

    class Meta:
        db_table = 'film'
        verbose_name = 'film'
        verbose_name_plural = 'films'

    def __str__(self):
        return self.name
