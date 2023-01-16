from django.db import models

from unidecode import unidecode


class Actor(models.Model):
    id = models.PositiveIntegerField(primary_key=True)
    name = models.CharField(max_length=100)

    def __str__(self) -> str:
        return self.name

    def get_unidecoded_name(self) -> str:
        return unidecode(self.name)


class Movie(models.Model):
    id = models.PositiveIntegerField(primary_key=True)
    title = models.CharField(max_length=100)
    actors = models.ManyToManyField(Actor, related_name="movies")

    def __str__(self) -> str:
        return self.title

    def get_unidecoded_title(self) -> str:
        return unidecode(self.title)
