from django.db import models


class Director(models.Model):
    name = models.CharField(max_length=100, help_text="Director name", default=None)
    
    class Meta:
        db_table = 'director'
        verbose_name = 'director'
        verbose_name_plural = 'directors'

    def __str__(self):
        return self.name


class Actor(models.Model):
    name = models.CharField(max_length=100, help_text="Actor name", default=None)
    
    class Meta:
        db_table = 'actor'
        ordering = ['name']
        verbose_name = 'actor'
        verbose_name_plural = 'actors'

    def __str__(self):
        return self.name


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
