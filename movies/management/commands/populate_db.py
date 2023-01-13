from django.core.management.base import BaseCommand
from movies.models import Actor, Movie
from movies.scrape_movies import scrape_csfd_movies
from movies.constants import MOVIE_COUNT

from typing import Any


class Command(BaseCommand):
    help = "Populate the database with films and actors"

    def handle(self, *args: Any, **options: Any) -> None:
        self.stdout.write(self.style.SUCCESS('Dumping the current database contents...'))
        films_actors = scrape_csfd_movies(MOVIE_COUNT)
        for film_actors in films_actors:
            film = Movie.objects.create(title=film_actors["name"])
            for actor_name in film_actors["actors"]:
                actor, _ = Actor.objects.get_or_create(name=actor_name)
                film.actors.add(actor)
