from django.db import models


class Actor(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self) -> str:
        return self.name


class Movie(models.Model):
    title = models.CharField(max_length=100)
    actors = models.ManyToManyField(Actor, related_name="movies")

    def __str__(self) -> str:
        return self.title
